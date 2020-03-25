library(Seurat)
library(ggplot2)
library(sctransform)
library(future)
library(Matrix)
memory.limit(size = 12000000000)
matrix1_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\DifferentDevelopmentalAges_sameBatch\\LH28141_87dM\\"
matrix1.path <- paste0(matrix1_dir, "matrix.mtx")
barcodes1.path <- paste0(matrix1_dir, "barcodes.tsv")
features1.path <- paste0(matrix1_dir, "features.tsv")
mat1 <- readMM(file = matrix1.path)
barcode1.names = read.delim(barcodes1.path, header = FALSE, stringsAsFactors = FALSE)
feature1.names = read.delim(features1.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat1) = barcode1.names$V1
rownames(mat1) = feature1.names$V1

matrix2_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\DifferentDevelopmentalAges_sameBatch\\LH28188_100dM\\"
matrix2.path <- paste0(matrix2_dir, "matrix.mtx")
barcodes2.path <- paste0(matrix2_dir, "barcodes.tsv")
features2.path <- paste0(matrix2_dir, "features.tsv")
mat2 <- readMM(file = matrix2.path)
barcode2.names = read.delim(barcodes2.path, header = FALSE, stringsAsFactors = FALSE)
feature2.names = read.delim(features2.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat2) = barcode2.names$V1
rownames(mat2) = feature2.names$V1

matrix3_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\DifferentDevelopmentalAges_sameBatch\\LH28195_122dF\\"
matrix3.path <- paste0(matrix3_dir, "matrix.mtx")
barcodes3.path <- paste0(matrix3_dir, "barcodes.tsv")
features3.path <- paste0(matrix3_dir, "features.tsv")
mat3 <- readMM(file = matrix3.path)
barcode3.names = read.delim(barcodes3.path, header = FALSE, stringsAsFactors = FALSE)
feature3.names = read.delim(features3.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat3) = barcode3.names$V1
rownames(mat3) = feature3.names$V1

matrix4_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\DifferentDevelopmentalAges_sameBatch\\H28190_135dM\\"
matrix4.path <- paste0(matrix4_dir, "matrix.mtx")
barcodes4.path <- paste0(matrix4_dir, "barcodes.tsv")
features4.path <- paste0(matrix4_dir, "features.tsv")
mat4 <- readMM(file = matrix4.path)
barcode4.names = read.delim(barcodes4.path, header = FALSE, stringsAsFactors = FALSE)
feature4.names = read.delim(features4.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat4) = barcode4.names$V1
rownames(mat4) = feature4.names$V1

matrix5_dir = "C:\\Users\\scsac\\Desktop\\GATech\\GhosnLab\\SachinKumar_GhosnLab Shared folder\\DifferentDevelopmentalAges_sameBatch\\H28159_142dF\\"
matrix5.path <- paste0(matrix5_dir, "matrix.mtx")
barcodes5.path <- paste0(matrix5_dir, "barcodes.tsv")
features5.path <- paste0(matrix5_dir, "features.tsv")
mat5 <- readMM(file = matrix5.path)
barcode5.names = read.delim(barcodes5.path, header = FALSE, stringsAsFactors = FALSE)
feature5.names = read.delim(features5.path, header = FALSE, stringsAsFactors = FALSE)
colnames(mat5) = barcode5.names$V1
rownames(mat5) = feature5.names$V1

rownames(barcode1.names) = barcode1.names$V1
rownames(barcode2.names) = barcode2.names$V1
rownames(barcode3.names) = barcode3.names$V1
rownames(barcode4.names) = barcode4.names$V1
rownames(barcode5.names) = barcode5.names$V1

da_87 <- CreateSeuratObject(counts = mat1, meta.data = barcode1.names, project = "D87")
da_87 <- SCTransform(da_87, verbose = FALSE)
da_87@meta.data$day <- "D87"

da_100 <- CreateSeuratObject(counts = mat2, meta.data = barcode2.names, project = "D100")
da_100 <- SCTransform(da_100, verbose = FALSE)
da_100@meta.data$day <- "D100"

da_122 <- CreateSeuratObject(counts = mat3, meta.data = barcode3.names, project = "D122")
da_122 <- SCTransform(da_122, verbose = FALSE)
da_122@meta.data$day <- "D122"

da_135 <- CreateSeuratObject(counts = mat4, meta.data = barcode4.names, project = "D135")
da_135 <- SCTransform(da_135, verbose = FALSE)
da_135@meta.data$day <- "D135"

da_142 <- CreateSeuratObject(counts = mat5, meta.data = barcode5.names, project = "D142")
da_142 <- SCTransform(da_142, verbose = FALSE)
da_142@meta.data$day <- "D142"

options(future.globals.maxSize = 16000 * 1024^2)

dages.features <- SelectIntegrationFeatures(object.list = list(da_87, da_100, da_122, da_135, da_142), nfeatures = 3000)
dages.list <- PrepSCTIntegration(object.list = list(da_87, da_100, da_122, da_135, da_142), anchor.features = dages.features, 
                                 verbose = FALSE)

dages.anchors <- FindIntegrationAnchors(object.list = dages.list, anchor.features = dages.features, normalization.method = "SCT", dims = 1:30)
dages.combined <- IntegrateData(anchorset = dages.anchors, normalization.method = "SCT", dims = 1:30)
DefaultAssay(dages.combined) <- "RNA"
dages.combined <- FindVariableFeatures(dages.combined, selection.method = "vst", nfeatures = 3000)
dages.combined <- ScaleData(dages.combined, verbose = FALSE)
dages.combined <- RunPCA(dages.combined, npcs = 30, verbose = FALSE)
# t-SNE and Clustering
dages.combined <- RunUMAP(dages.combined, dims = 1:30)
p1 <- DimPlot(dages.combined)
plot(p1)