import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, Union, Optional
import pandas as pd
import scanpy as sc
import bioquest
import pathlib

def dimplot(
    adata: sc.AnnData,
    reduction:str,
    filename:str,
    dim1:str='UMAP1',
    dim2:str='UMAP2',
    color:str="CellType",
    formats=("pdf", "png"),
    frameon:bool=False,
    outdir: Union[pathlib.PosixPath, str] = pathlib.Path().absolute(),
    width=7,
    height=6,
    dpi:int=300,
    **kwds
):
    _saveimg = bioquest.tl.saveimg(formats=formats, outdir=outdir, dpi=dpi)
    plt.rcParams["figure.figsize"] = (width, height)
    ax = sc.pl.embedding(
        adata,
        basis=reduction,
        color=color,
        show=False,
        frameon=frameon,
        **kwds
    )
    ax.arrow(
        -7,
        -12,
        5 * height / width,
        0,
        head_width=0.5,
        head_length=0.5,
        width=0.1,
        color="black",
    )
    ax.arrow(
        -7,
        -12,
        0,
        5,
        head_width=0.5,
        head_length=0.5,
        width=0.1 * height / width,
        color="black",
    )
    ax.text(-6.5, -13.5, dim1, fontdict=dict(weight="bold", color="black"))
    ax.text(-8, -11.3, dim2, fontdict={"fontweight": "bold", "rotation": "vertical"})
    _saveimg(filename=filename, figsize=(width, height))


def plot_batch_effect(
    adata: sc.AnnData,
    cluster_key: str,
    batch_key: str = "Sample",
    reduction:str='umap',
    resolution: float = 1.0,
    use_rep: Optional[str] = None,
    outdir: Union[pathlib.PosixPath, str] = pathlib.Path().absolute(),
    legend_loc: str = "right margin",  # right margin, on data,
    legend_fontsize: str = "small",  # [‘xx-small’, ‘x-small’, ‘small’, ‘medium’, ‘large’, ‘x-large’, ‘xx-large’]
    n_pcs: int = 20,
    pca_use_hvg: bool = True,
    n_neighbors: int = 15,
    dpi: int = 300,
    formats: tuple = ("pdf", "png"),
) -> Optional[sc.AnnData]:
    bioquest.tl.mkdir(outdir)
    _saveimg = bioquest.tl.saveimg(formats=formats, outdir=outdir, dpi=dpi)
    sc.tl.pca(adata, svd_solver="arpack", n_comps=50, use_highly_variable=pca_use_hvg)
    sc.pl.pca_variance_ratio(adata, n_pcs=50, show=False)
    _saveimg(f"PCA_variance_ratio")

    sc.pp.neighbors(adata, n_neighbors=n_neighbors, use_rep=use_rep, n_pcs=n_pcs)
    sc.tl.umap(adata)
    # batch_key='Sample';legend_loc='right margin';reduction='umap';outdir=f"{OUTDIR}/batch_effect_before_integratation"
    # legend_fontsize='small';cluster_key='Cluster_before_integratation'
    dimplot(
        adata,
        reduction=reduction,
        color=batch_key,
        legend_fontsize=legend_fontsize,
        filename=f"{batch_key}_{reduction}",
        outdir=outdir,
        legend_loc=legend_loc,
    )
    sc.tl.leiden(adata, key_added=cluster_key, resolution=resolution)
    dimplot(
        adata,
        reduction='umap',
        color=cluster_key,
        legend_loc=legend_loc,
        legend_fontsize=legend_fontsize,
        filename=f"{cluster_key}_{reduction}",
        outdir=outdir
    )