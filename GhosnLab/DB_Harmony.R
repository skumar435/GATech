library(harmony)
library(Seurat)
library(ggplot2)
library(sctransform)
library(future)
library(Matrix)
matrix1_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SeparateBatch\\Batch1- 4 samples\\PACH14Null\\"
matrix1.path <- paste0(matrix1_dir, "matrix.mtx")
barcodes1.path <- paste0(matrix1_dir, "barcodes.tsv")
genes1.path <- paste0(matrix1_dir, "genes.tsv")
mat1 <- readMM(file = matrix1.path)
barcode1.names = read.delim(barcodes1.path, header = FALSE, stringsAsFactors = FALSE)
gene1.names = read.delim(genes1.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat1) = barcode1.names$V1
rownames(mat1) = gene1.names$V1

matrix2_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SeparateBatch\\Batch1- 4 samples\\PACH14TNF\\"
matrix2.path <- paste0(matrix2_dir, "matrix.mtx")
barcodes2.path <- paste0(matrix2_dir, "barcodes.tsv")
genes2.path <- paste0(matrix2_dir, "genes.tsv")
mat2 <- readMM(file = matrix2.path)
barcode2.names = read.delim(barcodes2.path, header = FALSE, stringsAsFactors = FALSE)
gene2.names = read.delim(genes2.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat2) = barcode2.names$V1
rownames(mat2) = gene2.names$V1

matrix3_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SeparateBatch\\Batch1- 4 samples\\PACJ12Null\\"
matrix3.path <- paste0(matrix3_dir, "matrix.mtx")
barcodes3.path <- paste0(matrix3_dir, "barcodes.tsv")
genes3.path <- paste0(matrix3_dir, "genes.tsv")
mat3 <- readMM(file = matrix3.path)
barcode3.names = read.delim(barcodes3.path, header = FALSE, stringsAsFactors = FALSE)
gene3.names = read.delim(genes3.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat3) = barcode3.names$V1
rownames(mat3) = gene3.names$V1

matrix4_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SeparateBatch\\Batch1- 4 samples\\PACJ12TNF\\"
matrix4.path <- paste0(matrix4_dir, "matrix.mtx")
barcodes4.path <- paste0(matrix4_dir, "barcodes.tsv")
genes4.path <- paste0(matrix4_dir, "genes.tsv")
mat4 <- readMM(file = matrix4.path)
barcode4.names = read.delim(barcodes4.path, header = FALSE, stringsAsFactors = FALSE)
gene4.names = read.delim(genes4.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat4) = barcode4.names$V1
rownames(mat4) = gene4.names$V1

matrix5_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SeparateBatch\\Batch2- 4 samples\\PACJ13Null\\"
matrix5.path <- paste0(matrix5_dir, "matrix.mtx")
barcodes5.path <- paste0(matrix5_dir, "barcodes.tsv")
genes5.path <- paste0(matrix5_dir, "genes.tsv")
mat5 <- readMM(file = matrix5.path)
barcode5.names = read.delim(barcodes5.path, header = FALSE, stringsAsFactors = FALSE)
gene5.names = read.delim(genes5.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat5) = barcode5.names$V1
rownames(mat5) = gene5.names$V1

matrix6_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SeparateBatch\\Batch2- 4 samples\\PACJ13TNF\\"
matrix6.path <- paste0(matrix6_dir, "matrix.mtx")
barcodes6.path <- paste0(matrix6_dir, "barcodes.tsv")
genes6.path <- paste0(matrix6_dir, "genes.tsv")
mat6 <- readMM(file = matrix6.path)
barcode6.names = read.delim(barcodes6.path, header = FALSE, stringsAsFactors = FALSE)
gene6.names = read.delim(genes6.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat6) = barcode6.names$V1
rownames(mat6) = gene6.names$V1

matrix7_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SeparateBatch\\Batch2- 4 samples\\PACJ14Null\\"
matrix7.path <- paste0(matrix7_dir, "matrix.mtx")
barcodes7.path <- paste0(matrix7_dir, "barcodes.tsv")
genes7.path <- paste0(matrix7_dir, "genes.tsv")
mat7 <- readMM(file = matrix7.path)
barcode7.names = read.delim(barcodes7.path, header = FALSE, stringsAsFactors = FALSE)
gene7.names = read.delim(genes7.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat7) = barcode7.names$V1
rownames(mat7) = gene7.names$V1

matrix8_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\SeparateBatch\\Batch2- 4 samples\\PACJ14TNF\\"
matrix8.path <- paste0(matrix8_dir, "matrix.mtx")
barcodes8.path <- paste0(matrix8_dir, "barcodes.tsv")
genes8.path <- paste0(matrix8_dir, "genes.tsv")
mat8 <- readMM(file = matrix8.path)
barcode8.names = read.delim(barcodes8.path, header = FALSE, stringsAsFactors = FALSE)
gene8.names = read.delim(genes8.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat8) = barcode8.names$V1
rownames(mat8) = gene8.names$V1

rownames(barcode1.names) = barcode1.names$V1
rownames(barcode2.names) = barcode2.names$V1
rownames(barcode3.names) = barcode3.names$V1
rownames(barcode4.names) = barcode4.names$V1
rownames(barcode5.names) = barcode5.names$V1
rownames(barcode6.names) = barcode6.names$V1
rownames(barcode7.names) = barcode7.names$V1
rownames(barcode8.names) = barcode8.names$V1

dB <- CreateSeuratObject(counts = cbind(mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8), project = "DT", min.cells = 5) %>%
  Seurat::NormalizeData(verbose = FALSE) %>%
  FindVariableFeatures(selection.method = "vst", nfeatures = 2000) %>% 
  ScaleData(verbose = FALSE) %>% 
  RunPCA(pc.genes = dB@var.genes, npcs = 20, verbose = FALSE)

dB@meta.data$data <- c(rep("B1_1", ncol(mat1)), rep("B1_2", ncol(mat2)), rep("B1_3", ncol(mat3)), rep("B1_4", ncol(mat4)), rep("B2_1", ncol(mat5)), rep("B2_2", ncol(mat6)), rep("B2_3", ncol(mat7)), rep("B2_4", ncol(mat8)))
options(repr.plot.height = 2.5, repr.plot.width = 6)
dB <- dB %>% 
  RunHarmony("data", plot_convergence = TRUE)
harmony_embeddings <- Embeddings(dB, 'harmony')
options(repr.plot.height = 5, repr.plot.width = 12)
p1 <- DimPlot(object = dB, reduction = "harmony", pt.size = .1, group.by = "data", do.return = TRUE)
plot(p1)
dB <- dB %>% 
  RunUMAP(reduction = "harmony", dims = 1:20) %>% 
  FindNeighbors(reduction = "harmony", dims = 1:20) %>% 
  FindClusters(resolution = 0.5) %>% 
  identity()
options(repr.plot.height = 4, repr.plot.width = 10)
DimPlot(dB, reduction = "umap", group.by = "data", pt.size = .1, split.by = 'data')
options(repr.plot.height = 4, repr.plot.width = 6)
DimPlot(dB, reduction = "umap", label = TRUE, pt.size = .1)