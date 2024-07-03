import os, sys, string, argparse, re
import numpy as np
import pyqtgraph as pg
from glob import glob
from time import time
from qiplot.reader import get_xye
from qiplot.colors import getcmcolors
import logging
from logging.config import fileConfig

# Import PyQt5 or PyQt6
try:
    from PyQt5 import QtGui, QtCore, QtWidgets
    PYQT_VERSION = 5
except ImportError:
    from PyQt6 import QtGui, QtCore, QtWidgets
    from PyQt6.QtCore import QPointF as Point
    PYQT_VERSION = 6

#%%

class Qiplot:
    def __init__(self, title, size):
        ## initialise qt app
        self.app = pg.mkQApp()
        self.win = pg.GraphicsLayoutWidget(title=title)
        self.win.resize(size[0], size[1])
        self.win.show()
        self.label = pg.LabelItem(justify='right')
        self.win.addItem(self.label)
        self.plow = self.win.addPlot(row=1, col=0, name='p1')
        self.plow.showGrid(True, True, 0.5)
        ## add legend and set location
        self.leg = self.plow.addLegend()
        if PYQT_VERSION == 5:
            self.leg.autoAnchor(pg.Point(self.plow.width()*0.95, self.plow.height()*0.0))
        else:
            self.leg.setOffset((self.plow.width()*0.95, self.plow.height()*0.0))

    def _mouseMoved(self, evt):
        mousePoint = self.plow.vb.mapSceneToView(evt[0])
        self.label.setText(f"<span style='font-size: 14pt; color: white'> x={mousePoint.x():-10.4f} y={mousePoint.y():-10.4f}</span>")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Lightweight, file-based plotting for Linux and Windows')
    parser.add_argument('datafiles', nargs='+', type=str,
                        help='String(s) passed to glob to look for plottable files')
    parser.add_argument('-l','--label', choices=['index','prefix','dir','full'],
                        default='prefix', help='Cut legend label at: \
                        index (0002), prefix (Cr2O3_98keV_x1200_0002), dir (Cr2O3/Cr2O3_98keV_x1200_0002),\
                        full (/data/id15/inhouse3/2018/ch5514/Cr2O3/Cr2O3_98keV_x1200_0002)')
    parser.add_argument('-t','--title', default=os.path.realpath('.').split('/')[-1], help='Window title')
    parser.add_argument('-o', '--offset', default=0, nargs='?', type=float,
                        help='Offset every successive curve by an arbitrary value. Default: 0')
    parser.add_argument('--every', default=1, type=int, help='Plot only every N-th input file')
    parser.add_argument('--diff', default=None, type=int, const=0, nargs='?',
                        help='If True, plot the difference between each curve and the N-th input curve. \
                              Default (no value) = 0 (first curve). To subtract mean use --diff -99. \
                              Error is propagated over the two curves.')
    parser.add_argument('--usecols', default=None, type=int, nargs='*',
                        help='List of columns to extract from each input file. Default: [0,1,2], meaning x=0, y=1, e=2. \
                              If no error column is found, the reader switches automatically to [0,1]. \
                              In general, this is useful only when x is no the first column.')
    parser.add_argument('--maxbytes', type=int, nargs='?', default=-1,
                        help='Maximum size (in MB) to read from each file. This is useful when trying to read long files.')
    parser.add_argument('--cmap', type=str, default='spectral', nargs='?', help='One of the available matplotlib cmaps')
    parser.add_argument('--winsize', type=int, nargs=2, default=(1024,768), help='Plot window size in pixels as width and height. Default: 1024 768')
    return parser.parse_args()

def main():

    t0 = time()
    pg.setConfigOption('leftButtonPan', False)
    dname = glob(os.path.dirname(__file__))[0]
    cfgname = dname + '/logconf.py'
    fileConfig(cfgname)
    logging.info('Ready')

    ## read input files
    args = parse_arguments()
    print(args.usecols)
    data, names = get_xye(args.datafiles[::args.every], args.usecols, args.maxbytes*(1<<20), args.label)
    t1 = time()
    logging.info(f'Getting data:{np.round(t1-t0, 3)} s')

    ## start qt application
    colors = getcmcolors(len(data), args.cmap)
    qplot = Qiplot(args.title, args.winsize)
    t2 = time()
    logging.info(f'Initialising plot:{np.round(t2-t1, 3)} s')

    ## add curves to plot
    for ii in range(len(data)):
        x,y,e = data[ii][0], data[ii][1], data[ii][2]
        y += args.offset*ii
        if args.diff is not None and type(args.diff) == int:
            if args.diff != -99:
                ysubtr, esubtr = data[args.diff][1], data[args.diff][2]
            elif args.diff == -99:
                ysubtr, esubtr = np.mean(np.array(data)[:,1], axis=0), np.mean(np.array(data)[:,2], axis=0)
            y = y-ysubtr
            if sum(e) != 0:
                e = np.sqrt(e**2 + esubtr**2)
        cpen = pg.mkPen(colors[ii], width=1.25)
        li = pg.PlotDataItem(x=x, y=y, pen=cpen, name=names[ii])
        qplot.plow.addItem(li)
        if sum(e) != 0:
            e += args.offset*ii
            err = pg.ErrorBarItem(x=x, y=y, top=e/2, bottom=e/2, beam=0.5*np.mean(np.diff(x)), pen=cpen)
            qplot.plow.addItem(err)
    t3 = time()
    logging.info(f'Plotting:{np.round(t3-t2, 3)} s')

    ## add cursor position
    qplot.proxy = pg.SignalProxy(qplot.plow.scene().sigMouseMoved, rateLimit=60, slot=qplot._mouseMoved)

    ## launch qt application
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtWidgets.QApplication.instance()
        if app is None:
            app = QtWidgets.QApplication(sys.argv)
        if PYQT_VERSION == 5:
            app.exec_()
        else:
            app.exec()

if __name__ == '__main__':
    main()
