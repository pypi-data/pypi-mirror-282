# Rapid QC-MS
**Rapid QC-MS** is an all-in-one solution for automated quality control of liquid chromatography-mass spectrometry (LC-MS) instrument runs, both during and after data acquisition.

![](https://public.czbiohub.org/rapid-qc-ms-docs/Overview/rapidqcms-demo.gif)

It offers a fast, straightforward approach to ensure collection of high-quality data, allowing for less time investigating raw data and more time conducting experiments.

Developed at the [Mass Spectrometry Platform of CZ Biohub San Francisco](https://www.czbiohub.org/mass-spec/), Rapid QC-MS provides a host of key features to streamline untargeted metabolomics research, such as:

- **Automated and user-defined quality control checks** during instrument runs
- **Realtime updates on QC fails** in the form of Slack or email notifications
- **Interactive data visualization** of internal standard retention time, _m/z_, and intensity across samples
- **Google Drive cloud sync** and secure, Google-authenticated access to QC results from any device

![](https://public.czbiohub.org/rapid-qc-ms-docs/Home/intensity.png)
![](https://public.czbiohub.org/rapid-qc-ms-docs/Overview/RapidQCMS-BioStndDemo.gif)
![](https://public.czbiohub.org/rapid-qc-ms-docs/Overview/slack_example.png)

# Requirements
**Rapid QC-MS was designed to run on Windows platforms** because of its dependency on [MSConvert](https://proteowizard.sourceforge.io/tools/msconvert.html) for vendor format data conversion and [MS-DIAL](http://prime.psc.riken.jp/compms/msdial/main.html) for data processing and identification. However, MacOS users can still use Rapid QC-MS to monitor / view their instrument run data.

In addition, Rapid QC-MS requires Python 3.8 to 3.11 and various Python packages, including:

- Pandas
- SQLAlchemy
- Plotly Dash
- Bootstrap
- Watchdog
- Google API
- Slack API

These are installed automatically during setup.

**Note:** Installation of Python and various Python packages on MS instrument computers comes at no risk. For extra security and peace of mind, you can opt to install Rapid QC-MS in a virtual environment. To learn more, please read the [installation guide](https://czbiohub-sf.github.io/Rapid-QC-MS/installation.html#2-install-ms-autoqc).

# Installation
Installing Rapid QC-MS is easy. Simply open your Terminal or Command Prompt and enter:
```python
py -m pip install rapid-qc-ms
```

If you have multiple versions of python on your system, you can specifiy the version you want to use this way
```py -3.# -m pip install rapid-qc-ms```

Python dependencies are installed automatically, but dependencies such as MSConvert and MS-DIAL will need to be installed manually.

You can also opt to download and install Rapid QC-MS manually, or in a virtual environment if you prefer. Check out the [installation guide](https://czbiohub-sf.github.io/Rapid-QC-MS/installation.html#2-install-ms-autoqc) for more details.

[Example data](http://dx.doi.org/10.21228/M8Z119) can be downloaded from metabolomics workbench with [supplementary example files](https://doi.org/10.5281/zenodo.10525183) (sequence .csv, library .msp, and additional .raw files not published through workbench) available on zenodo.

# Usage
To start Rapid QC-MS, simply enter:
```python
rapidqcms
```

Check out the [quickstart guide](https://czbiohub-sf.github.io/Rapid-QC-MS/quickstart.html) to learn how easy setting up new QC jobs is.

![](https://public.czbiohub.org/rapid-qc-ms-docs/Overview/new_job_process.gif)

# Supported instrument vendors
Rapid QC-MS was designed to be a universal, open-source solution for data quality control. Because MSConvert converts raw acquired data into open mzML format before routing it to the data processing pipeline, the package will work seamlessly with data of all vendor formats.

**However, Rapid QC-MS has only been tested extensively on Thermo Fisher mass spectrometers, Thermo acquisition sequences, and Thermo RAW files.** As such, it is expected that there may be bugs and issues with processing data of other vendor formats.

If you encounter a bug, please report it by [opening an issue on GitHub](https://github.com/czbiohub-sf/Rapid-QC-MS/issues).

We are open to collaboration! If you would like to help us develop support for Agilent, Bruker, Sciex, or Waters acquisition sequences and data files, please send an email to [brian.defelice@czbiohub.org](mailto:brian.defelice@czbiohub.org).
