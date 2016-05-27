from flask import Flask
import importlib
import pandas as pd
import yaml
import json

app = Flask(__name__)

@app.route('/pkg_versions')
def pkg_versions():
    with open('environment.yml') as f:
        environment = yaml.load(f)
    versions = {}
    non_packages = {}
    for pkg_name in environment['dependencies']:
        try:
            pkg = importlib.import_module(pkg_name)
            versions[pkg_name] = pkg.__version__
        except Exception as e:
            non_packages[pkg_name] = str(e)
    return json.dumps({'package_versions':versions, 'non-python-packages':non_packages})


@app.route('/test_pandas')
def test_pandas():
    df = pd.DataFrame({'a':[1,2,3,4],'b':[9,10,0,0]})
    answer = {'df':df.to_dict(),
              'a_sum': df['a'].sum(),
              'a+b':(df['a']+df['b']).tolist(),
              'sum of a grouped by b': df.groupby('b')['a'].sum().to_dict()}
    return json.dumps(answer)


if __name__ == '__main__':
    app.run(debug = True)


