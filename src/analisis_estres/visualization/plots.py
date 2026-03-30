import matplotlib.pyplot as plt
import seaborn as sns


def apply_plot_style() -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)
