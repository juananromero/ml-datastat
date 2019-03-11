/*  by Juan A. Romero v1.0 26/02/2019*/
#include <stdio.h>
#include <string.h>

int ninstances(char *filename)
{
  FILE *data_file;
  char data_filename[50], c;
  int data_size, data_labels, data_features;
  strcpy(data_filename,"data/");
  strcat(data_filename,filename);
  data_file=fopen(data_filename, "r");
  fscanf(data_file,"%c %d \n", &c, &data_size);
  fscanf(data_file,"%c %d \n", &c, &data_features);
  fscanf(data_file,"%c %d \n", &c, &data_labels);
  printf("data_file: %s, instances: %d, features: %d, labels: %d \n",
   	  data_filename, data_size, data_features, data_labels);
  printf("\n");
  fclose(data_file);
}

int netiquetas(char *filename){
	FILE *data_file;
	char data_filename[50,c];
	int data_size, data_labels, data_features;
  strcpy(data_filename,"data/");
  strcat(data_filename,filename);
  data_file=fopen(data_filename, "r");
  fscanf(data_file,"%c %d \n", &c, &data_size);
  fscanf(data_file,"%c %d \n", &c, &data_features);
  fscanf(data_file,"%c %d \n", &c, &data_labels);
  printf("data_file: %s, labels: %d \n", data_filename, data_labels);
  printf("\n");
  fclose(data_file);
}
