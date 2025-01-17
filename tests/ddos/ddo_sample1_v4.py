#
# Copyright 2021 Ocean Protocol Foundation
# SPDX-License-Identifier: Apache-2.0
#
json_dict = {
    "@context": ["https://w3id.org/did/v1"],
    "id": "did:op:56c3d0ac76c02cc5cec98993be2b23c8a681800c08f2ff77d40c895907517280",
    "version": "4.1.0",
    "chainId": 1337,
    "nftAddress": "0xabc",
    "metadata": {
        "created": "2000-10-31T01:30:00.000-05:00Z",
        "updated": "2000-10-31T01:30:00.000-05:00",
        "name": "Ocean protocol white paper",
        "type": "dataset",
        "description": "Ocean protocol white paper -- description",
        "author": "Ocean Protocol Foundation Ltd.",
        "license": "CC-BY",
        "contentLanguage": "en-US",
        "tags": ["white-papers"],
        "additionalInformation": {"test-key": "test-value"},
        "links": [
            "http://data.ceda.ac.uk/badc/ukcp09/data/gridded-land-obs/gridded-land-obs-daily/",
            "http://data.ceda.ac.uk/badc/ukcp09/data/gridded-land-obs/gridded-land-obs-averages-25km/"
            "http://data.ceda.ac.uk/badc/ukcp09/",
        ],
    },
    "services": [
        {
            "id": "test",
            "type": "access",
            "datatokenAddress": "0xC7EC1970B09224B317c52d92f37F5e1E4fF6B687",
            "name": "Download service",
            "description": "Download service",
            "serviceEndpoint": "http://172.15.0.4:8030/",
            "timeout": 0,
            "files": "encryptedFiles",
        }
    ],
}
