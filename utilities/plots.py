import matplotlib.pyplot as plt
import numpy as np
from collections.abc import Iterable

def custom_subplots(*args, facecolor='#FFFFFFFF', size=None, **kwargs):
    """
    Create a custom subplot with specified facecolor and size.

    Parameters:
    - *args: Positional arguments for plt.subplots.
    - facecolor: Background color of the subplot.
    - size: Tuple specifying the size of the figure (width, height).
    - **kwargs: Additional keyword arguments for plt.subplots.

    Returns:
    - fig: The created figure.
    - axes: The created axes.
    """

    fig, axes = plt.subplots(*args, **kwargs)
    
    if size is not None:
        fig.set_size_inches(size)
    
    if not isinstance(axes, Iterable) or isinstance(axes, np.ndarray) and axes.ndim == 0:
        axes = [axes]
      
    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])

        for spine in ax.spines.values():
            spine.set_edgecolor('black')
            spine.set_linewidth(1)

    # Reduce the distance between the plotted images in the width
    plt.subplots_adjust(wspace=0.05)

    # Set the background colour of the figure
    fig.patch.set_facecolor(facecolor)

    axes = axes[0] if len(axes) == 1 else axes
    
    return fig, axes