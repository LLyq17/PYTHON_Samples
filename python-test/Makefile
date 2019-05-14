#--------------------------------

CMAKE_COMMAND = /usr/bin/cmake


all: dalitztoyfit_Ds3pi

include flags.make
%.cpp.o:  %.cpp flags.make
	@echo  "\033[32m Building CXX object $@ \033[0m"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o $@ -c $<
	
#DalitzFit_Ds3pi.cpp.o:flags.make DalitzFit_Ds3pi.cpp
#	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o DalitzFit_Ds3pi.cpp.o -c DalitzFit_Ds3pi.cpp


dalitztoyfit_Ds3pi:link.txt DalitzFit_Ds3pi.cpp.o
	@echo "\033[32m Linking CXX executable $@ \033[0m"
	$(CMAKE_COMMAND) -E cmake_link_script link.txt --verbose=$(VERBOSE)
	@echo "\033[32m $@ done \033[0m"

objects=dalitztoyfit_Ds3pi

clean:
	@rm  *.o $(objects)

.PHONY: clean
