PROJECT := report
BUILD_DIR := build

build: prepare compile_pdf copy_back clean

prepare:
	mkdir -p ${BUILD_DIR}

compile_pdf:
	pdflatex -output-directory=${BUILD_DIR} ${PROJECT}.tex

create_bibliography:
	bibtex ${BUILD_DIR}/${PROJECT}.aux

copy_back:
	cp ${BUILD_DIR}/${PROJECT}.pdf .

clean:
	rm -rf ${BUILD_DIR}
