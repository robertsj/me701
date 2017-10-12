def init_nice_plots() :
    from matplotlib import rcParams
    rcParams['font.family'] = 'serif'
    rcParams['font.serif'] = ['Times']
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'
    rcParams['xtick.labelsize'] = 18
    rcParams['ytick.labelsize'] = 18
    rcParams['ytick.left'] = True
    rcParams['ytick.right'] = True
    rcParams['ytick.left'] = True
    rcParams['ytick.right'] = True        
    rcParams['lines.linewidth'] = 1
    rcParams['axes.labelsize']  = 20
    #rcParams['axes.facecolor']  = 'white'
    rcParams['legend.fontsize'] = 16
    rcParams['figure.autolayout'] = True
    rcParams['text.usetex'] = True