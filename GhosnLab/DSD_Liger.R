library(devtools)
library(liger)
library(cowplot)
library(future)
library(Matrix)
memory.limit(size = 12000000000)

matrix1_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\Sample_5\\5GEX_PBMC1_36yoF_F1\\Batch1\\"
matrix1.path <- paste0(matrix1_dir, "matrix.mtx.gz")
barcodes1.path <- paste0(matrix1_dir, "barcodes.tsv.gz")
features1.path <- paste0(matrix1_dir, "features.tsv.gz")
mat1 <- readMM(file = matrix1.path)
barcode1.names = read.delim(barcodes1.path, header = FALSE, stringsAsFactors = FALSE)
feature1.names = read.delim(features1.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat1) = barcode1.names$V1
rownames(mat1) = feature1.names$V1

matrix2_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\Sample_5\\5GEX_PBMC1_36yoF_F1\\Batch2\\"
matrix2.path <- paste0(matrix2_dir, "matrix.mtx.gz")
barcodes2.path <- paste0(matrix2_dir, "barcodes.tsv.gz")
features2.path <- paste0(matrix2_dir, "features.tsv.gz")
mat2 <- readMM(file = matrix2.path)
barcode2.names = read.delim(barcodes2.path, header = FALSE, stringsAsFactors = FALSE)
feature2.names = read.delim(features2.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat2) = barcode2.names$V1
rownames(mat2) = feature2.names$V1

matrix3_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\Sample_5\\5GEX_PBMC3_46yoM_H1\\Batch1\\"
matrix3.path <- paste0(matrix3_dir, "matrix.mtx.gz")
barcodes3.path <- paste0(matrix3_dir, "barcodes.tsv.gz")
features3.path <- paste0(matrix3_dir, "features.tsv.gz")
mat3 <- readMM(file = matrix3.path)
barcode3.names = read.delim(barcodes3.path, header = FALSE, stringsAsFactors = FALSE)
feature3.names = read.delim(features3.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat3) = barcode3.names$V1
rownames(mat3) = feature3.names$V1

matrix4_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\Sample_5\\5GEX_PBMC3_46yoM_H1\\Batch2\\"
matrix4.path <- paste0(matrix4_dir, "matrix.mtx.gz")
barcodes4.path <- paste0(matrix4_dir, "barcodes.tsv.gz")
features4.path <- paste0(matrix4_dir, "features.tsv.gz")
mat4 <- readMM(file = matrix4.path)
barcode4.names = read.delim(barcodes4.path, header = FALSE, stringsAsFactors = FALSE)
feature4.names = read.delim(features4.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat4) = barcode4.names$V1
rownames(mat4) = feature4.names$V1

colnames(mat1) <- paste("F1B1", colnames(mat1), sep = "_")
colnames(mat2) <- paste("F1B2", colnames(mat2), sep = "_")
colnames(mat3) <- paste("H1B1", colnames(mat3), sep = "_")
colnames(mat4) <- paste("H1B2", colnames(mat4), sep = "_")

pbmc.data = list(f1b1=mat1, f1b2=mat2)
lObj.pbmc <- createLiger(pbmc.data)
lObj.pbmc <- normalize(lObj.pbmc)
lObj.pbmc <- selectGenes(lObj.pbmc, var.thresh = c(0.3, 0.875), do.plot = F)
lObj.pbmc <- scaleNotCenter(lObj.pbmc)
#k.suggest <- suggestK(lObj.pbmc, num.cores = 8, gen.new = T, plot.log2 = F,
#                      nrep = 5)
lObj.pbmc <- optimizeALS(lObj.pbmc, k=20, thresh = 5e-5, nrep = 3)
lObj.pbmc <- runTSNE(lObj.pbmc, use.raw = T)
p1 <- plotByDatasetAndCluster(lObj.pbmc, return.plots = T)
# Plot by dataset
print(p1[[1]])
lObj.pbmc <- quantile_norm(lObj.pbmc)
lObj.pbmc <- runTSNE(lObj.pbmc, dims = 1:15)
#p1 <- DimPlot(lObj.pbmc, reduction.use = "tsne", split.by = "")
#plot(p1)
p_a <- plotByDatasetAndCluster(lObj.pbmc, return.plots = T) 
# Modify plot output slightly
print(p_a[[1]])
print(p_a[[2]])
