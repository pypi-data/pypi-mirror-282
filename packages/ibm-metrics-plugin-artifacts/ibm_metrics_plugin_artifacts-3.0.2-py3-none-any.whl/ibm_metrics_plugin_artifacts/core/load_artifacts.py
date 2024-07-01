
# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# Licensed Materials - Property of IBM
# © Copyright IBM Corp. 2024  All Rights Reserved.
# US Government Users Restricted Rights -Use, duplication or disclosure restricted by
# GSA ADPSchedule Contract with IBM Corp.
# ----------------------------------------------------------------------------------------------------
import os

class LoadArtifacts:

    def load_dataset(self, dataset_name):

        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        
        # Construct the path to the dataset
        dataset_path = os.path.join(base_path, 'artifacts', 'datasets', dataset_name)

        # Read the JSON file
        with open(dataset_path, 'rb') as file:
            dataset = file.read()

        return dataset