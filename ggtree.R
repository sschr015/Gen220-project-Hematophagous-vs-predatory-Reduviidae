##Packages ----
library(ggplot2) #for creating graphs
library(ggtree) #addition to ggplot2 to better visualize and annotate trees, downloaded from Bioconductor, works only starting with R version 4 (not sure, 4.1 or 4.2)
library(treeio)#to import and export tree data
setwd("~/Desktop")


##Tree import ----
raxmltree <- read.iqtree('Align_trimmed.treefile.contree')
rootraxmltree <- root(raxmltree, outgroup = "Homalocoris_erythrogaster", resolve.root = T)

#Labeling taxa vector ----
rootraxmltree@phylo[["tip.label"]]

#Support values shown by color of branches ----
red_tree <- ggtree(rootraxmltree, aes(color=as.numeric(UFboot))) +
  geom_tiplab(color=c('red2', 'red2', 'black', 'black', 'black', 'black'), fontface = 3)+
  scale_color_gradient2(high='black', mid = 'red2', low='goldenrod2', midpoint = 50, limits=c(0, 100), guide_legend(title = "UF bootstrap")) +
  geom_text2(aes(label=UFboot, x=branch), vjust=-.3, size=3) +
  theme_tree() + ylim(1, 6) + xlim(0, 8)

ggsave('red_tree.tiff', plot = red_tree, scale = 1.5, height =5, width = 11, device='tiff', dpi=300,  units = c("cm"))

