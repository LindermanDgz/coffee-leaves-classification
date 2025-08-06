PROJECT := CoffeeLeavesClassification
SRC_DIR := src
BUILD_DIR := build

build: prepare compile_pdf create_bibliography compile_pdf copy_back clean

prepare:
	mkdir -p ${SRC_DIR}/${BUILD_DIR}

compile_pdf:
	cd ${SRC_DIR} && pdflatex -output-directory=${BUILD_DIR} ${PROJECT}.tex

create_bibliography:
	cd ${SRC_DIR} && bibtex ${BUILD_DIR}/${PROJECT}.aux

copy_back:
	cp ${SRC_DIR}/${BUILD_DIR}/${PROJECT}.pdf .

clean:
	rm -rf ${SRC_DIR}/${BUILD_DIR}
