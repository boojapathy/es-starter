OpenShift Elasticsearch Cartridge
=================================
This cartridge provides an Elasticsearch cluster as a standalone application with a kibana dashboard served and accessible by targetting the index page `/index.html`.

In order to create your application, first you need to register at Getup Cloud.
Go to http://getupcloud.com/#/sign-up and signup for free.
You receive a free 750h trial to test our services.

To create your Elasticsearch app, run:

    rhc app-create <app> https://raw.githubusercontent.com/boojapathy/es-starter/master/metadata/manifest.yml

Plugins
=======
To install Elasticsearch plugins, edit the `plugins.txt` file, commit, and push your changes.

    cd elasticsearch
    vim plugins.txt
    git commit -a -m 'Incluindo plugin XYZ'
    git push

You can also install plugins from a .zip file. Simply place it inside dir `plugins/`, git add, commit and push.

Configuration
=============
Configuration is build on-the-fly and starts with contents from file
`config/elasticsearch.yml.erb`, concatenated with any other files found in that
same dir (except for `logging.yml` and `elasticsearch.in.sh`). Files ending with
`.erb` will be pre-processed using ruby's erb command.

Credits
=======
Based on initial work from https://github.com/getupcloud/openshift-cartridge-elasticsearch

License
=======
This project is licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).
