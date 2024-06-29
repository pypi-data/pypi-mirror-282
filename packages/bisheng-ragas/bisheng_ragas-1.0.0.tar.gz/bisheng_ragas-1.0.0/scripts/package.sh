#!/bin/bash
repo="http://110.16.193.170:50083/repository/pypi-hosted/"

package() {
    rm -r dist
    pip install build
    python -m build
    echo "upload to file repository"
    twine upload --verbose -u deploy -p kDNubrlaK6n6RtzN --repository-url $repo dist/*.whl
}

download() {
    pip install bisheng-ragas -i https://public:26rS9HRxDqaVy5T@nx.dataelem.com/repository/pypi-hosted/simple
}

package
# download
