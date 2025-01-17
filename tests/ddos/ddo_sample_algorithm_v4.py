#
# Copyright 2021 Ocean Protocol Foundation
# SPDX-License-Identifier: Apache-2.0
#
algorithm_ddo_sample = {
    "@context": ["https://w3id.org/did/v1"],
    "id": "did:op:af051054d397c9d7f79dcca7391ba9f93941e99845ecf1ae132a3d203e450009",
    "version": "4.1.0",
    "chainId": 1337,
    "nftAddress": "0xabcd",
    "proof": {
        "created": "2019-02-08T08:13:41Z",
        "creator": "0x37BB53e3d293494DE59fBe1FF78500423dcFd43B",
        "signatureValue": "did:op:0bc278fee025464f8012b811d1bce8e22094d0984e4e49139df5d5ff7a028bdf",
        "type": "DDOIntegritySignature",
        "checksum": {
            "0": "0x52b5c93b82dd9e7ecc3d9fdf4755f7f69a54484941897dc517b4adfe3bbc3377",
            "1": "0x999999952b5c93b82dd9e7ecc3d9fdf4755f7f69a54484941897dc517b4adfe3",
        },
    },
    "metadata": {
        "created": "2019-02-08T08:13:49",
        "updated": "2019-02-08T08:13:49",
        "author": "John Doe",
        "license": "CC-BY",
        "name": "My super algorithm",
        "type": "algorithm",
        "description": "workflow for weather",
        "algorithm": {
            "language": "scala",
            "format": "docker-image",
            "version": "0.1",
            "container": {
                "entrypoint": "node $ALGO",
                "image": "node",
                "tag": "10",
                "checksum": "test",
            },
            "consumerParameters": [
                {
                    "name": "test_key",
                    "type": "string",
                    "label": "Test Key",
                    "required": False,
                    "description": "This is a test key",
                    "default": "some_value",
                    "options": ["some_value", "some_other_value"],
                },
                {
                    "name": "another_test_key",
                    "type": "string",
                    "label": "Another Test Key",
                    "required": False,
                    "description": "This is another test key",
                    "default": "some_other_value",
                },
            ],
        },
        "additionalInformation": {
            "description": "Workflow to aggregate weather information",
            "tags": ["weather", "uk", "2011", "workflow", "aggregation"],
            "copyrightHolder": "John Doe",
        },
    },
    "services": [
        {
            "id": "test",
            "type": "compute",
            "name": "dataAssetComputingService",
            "description": "dataAssetComputingService",
            "datatokenAddress": "0x20e91598bb797eEd2C7D4431a274c2997D080f53",
            "serviceEndpoint": "http://172.15.0.4:8030/",
            "timeout": 3600,
            "compute": {
                "namespace": "test",
                "allowRawAlgorithm": False,
                "allowNetworkAccess": False,
                "publisherTrustedAlgorithms": [],
                "publisherTrustedAlgorithmPublishers": [],
            },
            "files": "encryptedFiles",
            "consumerParameters": [
                {
                    "name": "test_key",
                    "type": "string",
                    "label": "Test Key",
                    "required": False,
                    "description": "This is a test key",
                    "default": "some_value",
                },
                {
                    "name": "another_test_key",
                    "type": "string",
                    "label": "Another Test Key",
                    "required": False,
                    "description": "This is another test key",
                    "default": "some_other_value",
                },
            ],
        }
    ],
}
