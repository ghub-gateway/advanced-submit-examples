#include <stdio.h>
#include "mpi.h"

int main( argc, argv )
	int  argc;
	char **argv;
{
	int rank, size;
	int len;
	char procname[MPI_MAX_PROCESSOR_NAME];
	MPI_Init( &argc, &argv );
	MPI_Comm_size( MPI_COMM_WORLD, &size );
	MPI_Comm_rank( MPI_COMM_WORLD, &rank );
	MPI_Get_processor_name(procname,&len);
	printf( "Hello world from process %d of %d on node  %s\n", rank, size, procname);
	MPI_Finalize();
	return 0;
}
