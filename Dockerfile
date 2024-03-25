FROM continuumio/miniconda3
ARG CONDA_REPO
RUN conda config --add channels $CONDA_REPO
RUN conda install hc
ENTRYPOINT ["python", "-m", "hc.server"]
