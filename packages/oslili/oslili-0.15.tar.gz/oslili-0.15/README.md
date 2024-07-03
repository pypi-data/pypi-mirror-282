# OSLiLi - Open Source License Identification Library

Open Source License Identification Library is an experimental code, that use Scikit-learn to implement a Multinomial Naive Bayes classifier trained with SPDX data to identify Open Source Licenses. This should be consider as a proof of concept for identify Open Source licenses using Machine Learning. 

This is an experimental project, please don't use it for production. For a more robust implementation, please check the project Askalono https://github.com/jpeddicord/askalono


## Usage

### On the command line

You can use OSLiLi in your terminal as command line, please install the oslili-cli package:
```
$ pip3 install oslili-cli
$ oslili-cli LICENSE
License: MIT (0.89 probability)
Copyright: ('2021', '(c)  Andrew Barrier')
```
### As a library

In order to use the library, you need to import and use identify_license or identify_copyright.
```
import argparse
from oslili import LicenseAndCopyrightIdentifier


def main():
    msg = 'Identify open source license and copyright statements'
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('file_path', help='Path to the file to analyze')
    args = parser.parse_args()
    file_path = args.file_path

    with open(args.file_path, 'r') as f:
        text = f.read()

    identifier = LicenseAndCopyrightIdentifier()
    license_spdx_code, license_proba = identifier.identify_license(text)
    print(f'License: {license_spdx_code} ({license_proba:.2f} probability)')
    year_range, statement = identifier.identify_copyright(text)
    if statement:
        if None not in statement:
            print(f'Copyright: {statement}')


if __name__ == '__main__':
    main()
```
## Notice

This tool does not provide legal advice; I'm not a lawyer.

The code is an experimental implementation to match your input to a database of similar license texts and tell you if it's a close match. Refrain from relying on the accuracy of the output of this tool.

Remember: The tool can't tell you if a license works for your project or use case. Please should seek independent legal advice for any licensing questions.

### Where do the licenses come from?

License SPDX dataset is sourced directly from SPDX: https://github.com/spdx/license-list-data. 

Datasets for ML training were generated scanning different sources, and inspired by two academic publications:

* [Machine Learning-Based Detection of Open Source License Exceptions](https://ieeexplore.ieee.org/document/7985655): C. Vendome, M. Linares-Vásquez, G. Bavota, M. Di Penta, D. German and D. Poshyvanyk, "Machine Learning-Based Detection of Open Source License Exceptions," 2017 IEEE/ACM 39th International Conference on Software Engineering (ICSE), Buenos Aires, 2017, pp. 118-129, doi: 10.1109/ICSE.2017.19.


* [A Machine Learning Method for Automatic Copyright Notice Identification of Source Files](https://www.jstage.jst.go.jp/article/transinf/E103.D/12/E103.D_2020EDL8089/_article): Shi QIU, German M. DANIEL, Katsuro INOUE, A Machine Learning Method for Automatic Copyright Notice Identification of Source Files, IEICE Transactions on Information and Systems, 2020, Volume E103.D, Issue 12, Pages 2709-2712, Released December 01, 2020, Online ISSN 1745-1361, Print ISSN 0916-853.



## Contributing

Contributions are very welcome! See [CONTRIBUTING](CONTRIBUTING.md) for more info.

## License

This library is licensed under the [Apache 2.0 License](LICENSE).