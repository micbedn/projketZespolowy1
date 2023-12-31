.. This file is automatically generated. Do not edit this file directly.

Cloud Healthcare API Python Samples
===============================================================================

.. image:: https://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&page=editor&open_in_editor=healthcare/api-client/v1/fhir/README.rst


This directory contains samples for Cloud Healthcare API. `Cloud Healthcare API`_ implements healthcare-native protocols and formats to accelerate ingestion, storage, analysis, and integration of healthcare data with cloud-based applications.
- See the `migration guide`_ for information about migrating to Python client library v0.25.1.

.. _migration guide: https://cloud.google.com/vision/docs/python-client-migration




.. _Cloud Healthcare API: https://cloud.google.com/healthcare/docs

To run the sample, you need to enable the API at: https://console.cloud.google.com/apis/library/healthcare.googleapis.com


To run the sample, you need to have the following roles:
* `Healthcare Dataset Administrator`
* `Healthcare FHIR Store Administrator`
* `Healthcare FHIR Resource Editor`



Setup
-------------------------------------------------------------------------------


Authentication
++++++++++++++

This sample requires you to have authentication setup. Refer to the
`Authentication Getting Started Guide`_ for instructions on setting up
credentials for applications.

.. _Authentication Getting Started Guide:
    https://cloud.google.com/docs/authentication/getting-started

Install Dependencies
++++++++++++++++++++

#. Clone python-docs-samples and change directory to the sample directory you want to use.

    .. code-block:: bash

        $ git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

#. Install `pip`_ and `virtualenv`_ if you do not already have them. You may want to refer to the `Python Development Environment Setup Guide`_ for Google Cloud Platform for instructions.

   .. _Python Development Environment Setup Guide:
       https://cloud.google.com/python/setup

#. Create a virtualenv. Samples are compatible with Python 2.7 and 3.4+.

    .. code-block:: bash

        $ virtualenv env
        $ source env/bin/activate

#. Install the dependencies needed to run the samples.

    .. code-block:: bash

        $ pip install -r requirements.txt

.. _pip: https://pip.pypa.io/
.. _virtualenv: https://virtualenv.pypa.io/

Samples
-------------------------------------------------------------------------------

FHIR stores
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. image:: https://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&page=editor&open_in_editor=healthcare/api-client/v1/fhir/fhir_stores.py,healthcare/api-client/v1/fhir/README.rst




To run this sample:

.. code-block:: bash

    $ python fhir_stores.py

    usage: fhir_stores.py [-h] [--project_id PROJECT_ID] [--location LOCATION]
                          [--dataset_id DATASET_ID]
                          [--fhir_store_id FHIR_STORE_ID]
                          [--pubsub_topic PUBSUB_TOPIC] [--gcs_uri GCS_URI]
                          [--member MEMBER] [--role ROLE]
                          {create-fhir-store,delete-fhir-store,get-fhir-store,get-fhir-store-metadata,list-fhir-stores,patch-fhir-store,import-fhir-resources,export-fhir-store-gcs,get_iam_policy,set_iam_policy}
                          ...

    positional arguments:
      {create-fhir-store,delete-fhir-store,get-fhir-store,get-fhir-store-metadata,list-fhir-stores,patch-fhir-store,import-fhir-resources,export-fhir-store-gcs,get_iam_policy,set_iam_policy}
        create-fhir-store   Creates a new FHIR store within the parent dataset.
                            See https://github.com/GoogleCloudPlatform/python-
                            docs-samples/tree/main/healthcare/api-client/v1/fhir
                            before running the sample.
        delete-fhir-store   Deletes the specified FHIR store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        get-fhir-store      Gets the specified FHIR store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        get-fhir-store-metadata
                            Gets the FHIR capability statement (STU3, R4), or the
                            conformance statement in the DSTU2 case for the store,
                            which contains a description of functionality
                            supported by the server. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        list-fhir-stores    Lists the FHIR stores in the given dataset. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        patch-fhir-store    Updates the FHIR store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        import-fhir-resources
                            Import resources into the FHIR store by copying them
                            from the specified source. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        export-fhir-store-gcs
                            Export resources to a Google Cloud Storage bucket by
                            copying them from the FHIR store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        get_iam_policy      Gets the IAM policy for the specified FHIR store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        set_iam_policy      Sets the IAM policy for the specified FHIR store. A
                            single member will be assigned a single role. A member
                            can be any of: - allUsers, that is, anyone -
                            allAuthenticatedUsers, anyone authenticated with a
                            Google account - user:email, as in
                            'user:somebody@example.com' - group:email, as in
                            'group:admins@example.com' - domain:domainname, as in
                            'domain:example.com' - serviceAccount:email, as in
                            'serviceAccount:my-other-
                            app@appspot.gserviceaccount.com' A role can be any IAM
                            role, such as 'roles/viewer', 'roles/owner', or
                            'roles/editor' See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.

    options:
      -h, --help            show this help message and exit
      --project_id PROJECT_ID
                            GCP cloud project name
      --location LOCATION   GCP location
      --dataset_id DATASET_ID
                            Name of dataset
      --fhir_store_id FHIR_STORE_ID
                            Name of FHIR store
      --pubsub_topic PUBSUB_TOPIC
                            The Cloud Pub/Sub topic where notifications of changes
                            are published
      --gcs_uri GCS_URI     URI for a Google Cloud Storage directory from which
                            filesshould be import or to which result filesshould
                            be written (e.g., "bucket-
                            id/path/to/destination/dir").
      --member MEMBER       Member to add to IAM policy (e.g.
                            "domain:example.com")
      --role ROLE           IAM Role to give to member (e.g. "roles/viewer")



FHIR resources
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. image:: https://gstatic.com/cloudssh/images/open-btn.png
   :target: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&page=editor&open_in_editor=healthcare/api-client/v1/fhir/fhir_resources.py,healthcare/api-client/v1/fhir/README.rst




To run this sample:

.. code-block:: bash

    $ python fhir_resources.py

    usage: fhir_resources.py [-h] [--project_id PROJECT_ID] [--location LOCATION]
                             [--dataset_id DATASET_ID]
                             [--fhir_store_id FHIR_STORE_ID]
                             [--resource_file RESOURCE_FILE]
                             [--resource_type RESOURCE_TYPE]
                             [--resource_id RESOURCE_ID] [--patient_id PATIENT_ID]
                             [--encounter_id ENCOUNTER_ID] [--bundle BUNDLE]
                             [--uri_prefix URI_PREFIX] [--version_id VERSION_ID]
                             [--structure_definition_file STRUCTURE_DEFINITION_FILE]
                             [--profile_url PROFILE_URL]
                             [--implementation_guide_file IMPLEMENTATION_GUIDE_FILE]
                             [--implementation_guide_url IMPLEMENTATION_GUIDE_URL]
                             {create-resource-from-file,create-patient,create-encounter,create-observation,delete-resource,get-resource,list-resource-history,execute-bundle,get-resource-history,delete-resource-purge,update-resource,patch-resource,search-resources-get,search-resources-post,get-patient-everything,create-structure-definition,create-implementation-guide,enable-implementation-guide,validate-resource,validate-resource-profile-url}
                             ...

    positional arguments:
      {create-resource-from-file,create-patient,create-encounter,create-observation,delete-resource,get-resource,list-resource-history,execute-bundle,get-resource-history,delete-resource-purge,update-resource,patch-resource,search-resources-get,search-resources-post,get-patient-everything,create-structure-definition,create-implementation-guide,enable-implementation-guide,validate-resource,validate-resource-profile-url}
        create-resource-from-file
                            Creates a new FHIR resource in a FHIR store from a
                            JSON resource file. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#create for the Python API reference.
                            Args: project_id: The project ID or project number of
                            the Cloud project you want to use. location: The name
                            of the parent dataset's location. dataset_id: The name
                            of the parent dataset. fhir_store_id: The name of the
                            FHIR store. resource_type: A valid FHIR resource type.
                            See https://www.hl7.org/fhir/resourcelist.html.
                            resource_file: The path to a JSON file containing a
                            FHIR resource. Returns: A dict representing the
                            created FHIR resource.
        create-patient      Creates a new Patient resource in a FHIR store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#create for the Python API reference.
                            Args: project_id: The project ID or project number of
                            the Cloud project you want to use. location: The name
                            of the parent dataset's location. dataset_id: The name
                            of the parent dataset. fhir_store_id: The name of the
                            FHIR store that holds the Patient resource. Returns: A
                            dict representing the created Patient resource.
        create-encounter    Creates a new Encounter resource in a FHIR store that
                            references a Patient resource. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#create for the Python API reference.
                            Args: project_id: The project ID or project number of
                            the Cloud project you want to use. location: The name
                            of the parent dataset's location. dataset_id: The name
                            of the parent dataset. fhir_store_id: The name of the
                            FHIR store. patient_id: The "logical id" of the
                            referenced Patient resource. The ID is assigned by the
                            server. Returns: A dict representing the created
                            Encounter resource.
        create-observation  Creates a new Observation resource in a FHIR store
                            that references an Encounter and Patient resource. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#create for the Python API reference.
                            Args: project_id: The project ID or project number of
                            the Cloud project you want to use. location: The name
                            of the parent dataset's location. dataset_id: The name
                            of the parent dataset. fhir_store_id: The name of the
                            FHIR store. patient_id: The "logical id" of the
                            referenced Patient resource. The ID is assigned by the
                            server. encounter_id: The "logical id" of the
                            referenced Encounter resource. The ID is assigned by
                            the server. Returns: A dict representing the created
                            Observation resource.
        delete-resource     Deletes a FHIR resource. Regardless of whether the
                            operation succeeds or fails, the server returns a 200
                            OK HTTP status code. To check that the resource was
                            successfully deleted, search for or get the resource
                            and see if it exists. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#delete for the Python API reference.
                            Args: project_id: The project ID or project number of
                            the Cloud project you want to use. location: The name
                            of the parent dataset's location. dataset_id: The name
                            of the parent dataset. fhir_store_id: The name of the
                            FHIR store. resource_type: The type of the FHIR
                            resource. resource_id: The "logical id" of the FHIR
                            resource you want to delete. The ID is assigned by the
                            server. Returns: An empty dict.
        get-resource        Gets the contents of a FHIR resource. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#read for the Python API reference.
                            Args: project_id: The project ID or project number of
                            the Cloud project you want to use. location: The name
                            of the parent dataset's location. dataset_id: The name
                            of the parent dataset. fhir_store_id: The name of the
                            FHIR store. resource_type: The type of FHIR resource.
                            resource_id: The "logical id" of the resource you want
                            to get the contents of. The ID is assigned by the
                            server. Returns: A dict representing the FHIR
                            resource.
        list-resource-history
                            Gets the history of a resource. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#history for the Python API
                            reference. Args: project_id: The project ID or project
                            number of the Cloud project you want to use. location:
                            The name of the parent dataset's location. dataset_id:
                            The name of the parent dataset. fhir_store_id: The
                            name of the FHIR store. resource_type: The type of
                            FHIR resource. resource_id: The "logical id" of the
                            resource whose history you want to list. The ID is
                            assigned by the server. Returns: A dict representing
                            the FHIR resource.
        execute-bundle      Executes the operations in the given bundle. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        get-resource-history
                            Gets the contents of a version (current or historical)
                            of a FHIR resource by version ID. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#vread for the Python API reference.
                            Args: project_id: The project ID or project number of
                            the Cloud project you want to use. location: The name
                            of the parent dataset's location. dataset_id: The name
                            of the parent dataset. fhir_store_id: The name of the
                            FHIR store. resource_type: The type of FHIR resource.
                            resource_id: The "logical id" of the resource whose
                            details you want to view at a particular version. The
                            ID is assigned by the server. version_id: The ID of
                            the version. Changes whenever the FHIR resource is
                            modified. Returns: A dict representing the FHIR
                            resource at the specified version.
        delete-resource-purge
                            Deletes all versions of a FHIR resource (excluding the
                            current version). See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#Resource_purge for the Python API
                            reference. Args: project_id: The project ID or project
                            number of the Cloud project you want to use. location:
                            The name of the parent dataset's location. dataset_id:
                            The name of the parent dataset. fhir_store_id: The
                            name of the FHIR store. resource_type: The type of the
                            FHIR resource. resource_id: The "logical id" of the
                            resource. The ID is assigned by the server. Returns:
                            An empty dict.
        update-resource     Updates the entire contents of a FHIR resource.
                            Creates a new current version if the resource already
                            exists, or creates a new resource with an initial
                            version if no resource already exists with the
                            provided ID. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#update for the Python API reference.
                            Args: project_id: The project ID or project number of
                            the Cloud project you want to use. location: The name
                            of the parent dataset's location. dataset_id: The name
                            of the parent dataset. fhir_store_id: The name of the
                            FHIR store. resource_type: The type of the FHIR
                            resource. resource_id: The "logical id" of the
                            resource. The ID is assigned by the server. Returns: A
                            dict representing the updated FHIR resource.
        patch-resource      Updates part of an existing FHIR resource by applying
                            the operations specified in a [JSON
                            Patch](http://jsonpatch.com/) document. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample. See
                            https://googleapis.github.io/google-api-python-client/
                            docs/dyn/healthcare_v1.projects.locations.datasets.fhi
                            rStores.fhir.html#patch for the Python API reference.
                            Args: project_id: The project ID or project number of
                            the Cloud project you want to use. location: The name
                            of the parent dataset's location. dataset_id: The name
                            of the parent dataset. fhir_store_id: The name of the
                            FHIR store. resource_type: The type of the FHIR
                            resource. resource_id: The "logical id" of the
                            resource. The ID is assigned by the server. Returns: A
                            dict representing the patched FHIR resource.
        search-resources-get
                            Uses the searchResources GET method to search for
                            resources in the given FHIR store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        search-resources-post
                            Uses the searchResources GET method to search for
                            resources in the given FHIR store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        get-patient-everything
                            Gets all the resources in the patient compartment. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        create-structure-definition
                            Creates a new StructureDefinition resource in a FHIR
                            store from a StructureDefinition JSON file. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        create-implementation-guide
                            Creates a new ImplementationGuide resource in a FHIR
                            store from an ImplementationGuide JSON file. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        enable-implementation-guide
                            Patches an existing FHIR store to enable an
                            ImplementationGuide resource that exists in the FHIR
                            store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        validate-resource   Validates an input FHIR resource's conformance to the
                            base profile configured on the FHIR store. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.
        validate-resource-profile-url
                            Validates an input FHIR resource's conformance to a
                            profile URL. The profile StructureDefinition resource
                            must exist in the FHIR store before performing
                            validation against the URL. See
                            https://github.com/GoogleCloudPlatform/python-docs-
                            samples/tree/main/healthcare/api-client/v1/fhir before
                            running the sample.

    options:
      -h, --help            show this help message and exit
      --project_id PROJECT_ID
                            GCP project name
      --location LOCATION   GCP location
      --dataset_id DATASET_ID
                            Name of dataset
      --fhir_store_id FHIR_STORE_ID
                            Name of FHIR store
      --resource_file RESOURCE_FILE
                            A JSON file containing the contents of a FHIR resource
                            to create
      --resource_type RESOURCE_TYPE
                            The type of resource. First letter must be capitalized
      --resource_id RESOURCE_ID
                            Identifier for a FHIR resource
      --patient_id PATIENT_ID
                            Identifier for a Patient resource. Can be used as a
                            reference for an Encounter/Observation
      --encounter_id ENCOUNTER_ID
                            Identifier for an Encounter resource. Can be used as a
                            reference for an Observation
      --bundle BUNDLE       Name of file containing bundle of operations to
                            execute
      --uri_prefix URI_PREFIX
                            Prefix of gs:// URIs for import and export
      --version_id VERSION_ID
                            Version of a FHIR resource
      --structure_definition_file STRUCTURE_DEFINITION_FILE
                            A StructureDefinition resource JSON file
      --profile_url PROFILE_URL
                            The canonical URL of the FHIR profile to validate
                            against
      --implementation_guide_file IMPLEMENTATION_GUIDE_FILE
                            An ImplementationGuide resource JSON file
      --implementation_guide_url IMPLEMENTATION_GUIDE_URL
                            the URL defined in the 'url' property of the
                            ImplementationGuide resource





The client library
-------------------------------------------------------------------------------

This sample uses the `Google Cloud Client Library for Python`_.
You can read the documentation for more details on API usage and use GitHub
to `browse the source`_ and  `report issues`_.

.. _Google Cloud Client Library for Python:
    https://googlecloudplatform.github.io/google-cloud-python/
.. _browse the source:
    https://github.com/GoogleCloudPlatform/google-cloud-python
.. _report issues:
    https://github.com/GoogleCloudPlatform/google-cloud-python/issues


.. _Google Cloud SDK: https://cloud.google.com/sdk/