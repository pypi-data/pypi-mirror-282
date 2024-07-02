

# TADGATE




Topologically associating domains (TADs) have emerged as basic structural and functional units of genome organization. However, accurately identifying TADs from sparse chromatin contact maps remain challenging. Here, we developed TADGATE to identify TADs in Hi-C contact map with a graph attention autoencoder. It can impute and smooth the sparse chromatin contact maps while preserving or enhancing their topological domains. TADGATE can output imputed Hi-C contact maps with clear topological structures. Additionally, it can provide embeddings for each chromatin bin, and the learned attention patterns can effectively depict the positions of TAD boundaries.



## Overview

TADGATE consists of several steps:

1. Construct a neighborhood graph to reflect the adjacency relationship of chromatin bins in the genome.
2. Each bin serves as a sample and its interaction vector serves as the sample feature. We train a  graph attention autoencoder with the pre-defined neighborhood graph (green layers with graph attention) to reconstruct the interaction vector of each bin.  
3. We can get the embeddings for each chromatin bin and all the reconstructed interaction vectors constitute the imputed map.  The valleys in the attention sum profile of the attention map correspond well to the TAD boundaries in the contact map.
4. We can combine the original and the imputed Hi-C contact maps, the embeddings of chromatin bins, and attention patterns learned by the model to identify TADs.

![TADGATE_overview](.\TADGATE_overview.png)



TADGATE can provide good embeddings to represent bins within each TAD.

<img src=".\TADGATE_embeddings.png" alt="TADGATE_embeddings" style="zoom:12%;" />

TADGATE can impute the sparse chromatin contact maps with enhanced topological domains.

<img src=".\TADGATE_imputed.png" alt="TADGATE_imputed" style="zoom:15%;" />

</p>

## Getting start

### Installation

The TADGATE package is developed based on the Python libraries [Scanpy](https://scanpy.readthedocs.io/en/stable/), [PyTorch](https://pytorch.org/) and [PyG](https://github.com/pyg-team/pytorch_geometric) (*PyTorch Geometric*) framework, and can be run on GPU (recommend) or CPU.



First clone the repository. 

~~~
git clone https://github.com/zhanglabtools/TADGATE.git
cd TADGATE
~~~

It's recommended to create a separate conda environment for running TADGATE:

```shell
#create an environment
conda create -n TADGATE python=3.8
#activate your environment
conda activate TADGATE
```



Install required packages:

```shell
pip install -r requirement.txt
```

If you can't install all the dependency packages at once, please try installing the Python packages listed in requirements.txt one by one. 

For pytorch-related packages, please see https://pytorch.org/ and torch-geometric library is also required, please see the installation steps in https://github.com/pyg-team/pytorch_geometric#installation

The use of the mclust algorithm requires the rpy2 package (Python) and the mclust package (R). See https://pypi.org/project/rpy2/ and https://cran.r-project.org/web/packages/mclust/index.html for detail.



Install TADGATE with two methods:

Method1: Install from source code:

~~~
python setup.py build
python setup.py install
~~~

Method2: Install TADGATE by PyPI

```shell
pip install TADGATE
```



### Example usage

See [TADGATE usage.ipynb](./TADGATE%20usage.ipynb).

### Support

If you have any issues, please let us know. We have a mailing list located at:

* dangdachang@163.com

### Citation

If TADGATE is useful for your research, consider citing our preprint:

> Uncovering topologically associating domains from three-dimensional genome maps with TADGATE.
> Dachang Dang, Shao-Wu Zhang, Kangning Dong, Ran Duan, Shihua Zhang
