install.packages("Seurat")
library(Seurat)
library(ggplot2)
library(sctransform)
library(future)
library(Matrix)
options(future.globals.maxSize = 4000 * 1024^2)
matrix1_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SameTissues_SameBatch\\PBMC_sameBatch\\PBMC 5\\filtered_feature_bc_matrix\\"
matrix1.path <- paste0(matrix1_dir, "matrix.mtx")
barcodes1.path <- paste0(matrix1_dir, "barcodes.tsv")
genes1.path <- paste0(matrix1_dir, "genes.tsv")
mat1 <- readMM(file = matrix1.path)
barcode1.names = read.delim(barcodes1.path, header = FALSE, stringsAsFactors = FALSE)
gene1.names = read.delim(genes1.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat1) = barcode1.names$V1
rownames(mat1) = gene1.names$V1

matrix2_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SameTissues_SameBatch\\PBMC_sameBatch\\PBMC 6\\filtered_feature_bc_matrix\\"
matrix2.path <- paste0(matrix2_dir, "matrix.mtx")
barcodes2.path <- paste0(matrix2_dir, "barcodes.tsv")
genes2.path <- paste0(matrix2_dir, "genes.tsv")
mat2 <- readMM(file = matrix2.path)
barcode2.names = read.delim(barcodes2.path, header = FALSE, stringsAsFactors = FALSE)
gene2.names = read.delim(genes2.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat2) = barcode2.names$V1
rownames(mat2) = gene2.names$V1

matrix3_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SameTissues_SameBatch\\PBMC_sameBatch\\PBMC 7\\filtered_feature_bc_matrix\\"
matrix3.path <- paste0(matrix3_dir, "matrix.mtx")
barcodes3.path <- paste0(matrix3_dir, "barcodes.tsv")
genes3.path <- paste0(matrix3_dir, "genes.tsv")
mat3 <- readMM(file = matrix3.path)
barcode3.names = read.delim(barcodes3.path, header = FALSE, stringsAsFactors = FALSE)
gene3.names = read.delim(genes3.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat3) = barcode3.names$V1
rownames(mat3) = gene3.names$V1

rownames(barcode1.names) = barcode1.names$V1
rownames(barcode2.names) = barcode2.names$V1
rownames(barcode3.names) = barcode3.names$V1

pbmc5 <- CreateSeuratObject(counts = mat1, meta.data = barcode1.names, project = "pbmc5")
pbmc5 <- SCTransform(pbmc5, verbose = FALSE)
pbmc5@meta.data$pbmc <- "PBMC5"

pbmc6 <- CreateSeuratObject(counts = mat2, meta.data = barcode2.names, project = "pbmc6")
pbmc6 <- SCTransform(pbmc6, verbose = FALSE)
pbmc6@meta.data$pbmc <- "PBMC6"

pbmc7 <- CreateSeuratObject(counts = mat3, meta.data = barcode3.names, project = "pbmc7")
pbmc7 <- SCTransform(pbmc7, verbose = FALSE)
pbmc7@meta.data$pbmc <- "PBMC7"

sameBatch.features <- SelectIntegrationFeatures(object.list = list(pbmc5, pbmc6, pbmc7), nfeatures = 3000)
sameBatch.list <- PrepSCTIntegration(object.list = list(pbmc5, pbmc6, pbmc7), anchor.features = sameBatch.features, 
                                    verbose = FALSE)
sameBatch.anchors <- FindIntegrationAnchors(object.list = sameBatch.list, normalization.method = "SCT", anchor.features = sameBatch.features, dims = 1:30)
sameBatch.combined <- IntegrateData(anchorset = sameBatch.anchors, normalization.method = "SCT", dims = 1:30)

sameBatch.combined <- ScaleData(sameBatch.combined, verbose = FALSE)
sameBatch.combined <- RunPCA(sameBatch.combined, npcs = 30, verbose = FALSE)
# t-SNE and Clustering
sameBatch.combined <- RunTSNE(sameBatch.combined, dims = 1:15)
sameBatch.combined <- FindNeighbors(sameBatch.combined, reduction = "pca", dims = 1:15)
sameBatch.combined <- FindClusters(sameBatch.combined, resolution = 0.6)
# Visualization
p2 <- DimPlot(sameBatch.combined, reduction.use = 'tsne', split.by = "pbmc")
plot(p2)