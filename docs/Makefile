PROJECT := CoffeeLeavesClassification
SRC_DIR := src
BUILD_DIR := build
MINTED_DIR := _minted-${PROJECT}

build:
	$(MAKE) prepare
	$(MAKE) compile_pdf
	$(MAKE) create_bibliography
	$(MAKE) compile_pdf
	$(MAKE) compile_pdf
	$(MAKE) copy_back
	$(MAKE) clean

prepare:
	mkdir -p ${SRC_DIR}/${BUILD_DIR}

compile_pdf:
	cd ${SRC_DIR} && pdflatex -shell-escape -output-directory=${BUILD_DIR} ${PROJECT}.tex

create_bibliography:
	cd ${SRC_DIR} && bibtex ${BUILD_DIR}/${PROJECT}.aux

copy_back:
	cp ${SRC_DIR}/${BUILD_DIR}/${PROJECT}.pdf .

clean:
	rm -rf ${SRC_DIR}/${BUILD_DIR}
	rm -rf ${SRC_DIR}/${MINTED_DIR}
