# Create CSV with sampled CDC data
vaccines:
	python -B src/vaccines.py

# Create CSV with JHU data
deaths:
	python -B src/deaths.py

# Create a CSV from merged vaccines and deaths CSVs
merge:
	python -B src/merge.py

# Create sample figures
figs:
	mkdir -p figs
	python -B src/figs.py

# Add a "clean"
clean:
	rm -r figs
