# Luke Lai
# 1355154
# luelai
# 5/6/15
# CS101
# Allen Van Gelder
# Makefile
# Makefile for pa02

# See Cmake/Makefile for a complete commented sample Makefile,
# illustrating separate compilation and dependencies.

# Running "make" can generate many error messages.  Do
#	make intList.o >& make.log
# to compile intList.c and cause the errors to go into the file make.log.
# When "make" finishes you can read the file with "view", "more", or "less".
#
# Many later error messages can be meaningless because they were caused
# by an earlier error.  Always try to correct errors in order.
#
# Do 
#       make graph01 >& make.log
# to create the executable file graph01.
#
# ===================================================================

CC     = gcc
CFLAGS = -g -Wall -O0
OUTPUT = scc03 test.txt

scc03:  scc03.o intList.o dfsTrace1.o dfsPhase2.o
	${CC}  -o scc03 scc03.o intList.o dfsTrace1.o dfsPhase2.o

intList.o:	intList.c  intList.h
	${CC}  -c  ${CFLAGS}  intList.c

dfsTrace1.o: dfsTrace1.c dfsTrace1.h
	${CC}  -c  ${CFLAGS} dfsTrace1.c

scc03.o:	scc03.c  intList.h 
	${CC}  -c  ${CFLAGS}  scc03.c

dfsPhase2.o:	dfsPhase2.c  dfsPhase2.h
	${CC}  -c  ${CFLAGS}  dfsPhase2.c

test: ${OUTPUT}
	./${OUTPUT}

clean: 
	rm -f *.o

spotless: clean
	rm -f ${OUTPUT}

.PHONY: clean spotles test

