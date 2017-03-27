.PHONY: exec

exec:
	export LANG=ja_JP.UTF-8
	CLASSPATH=gephi-toolkit-0.9.1-all.jar jython  headless_sample.py

