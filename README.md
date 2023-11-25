# python_sdk
[![LinkedIn][linkedin-shield]][https://www.linkedin.com/in/shahbaz-mahmood-660a76166/]



<h3 align="center">batch_debugging</h3>

  <p align="center">
    A python library that assists in debugging batch compute enviornments in AWS, GCP and Azure and Kubernetes
    <br />
    <a href="https://github.com/Shahbaz-mahmood123/batch-debugging"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a> -->
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <!-- <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul> -->
    </li>
    <li>
      <a href="#installation">Installation</a>
      <ul>
        <li><a href="#getting-started">Getting Started</a></li>
        <!-- <li><a href="#prerequisites">Prerequisites</a></li> -->
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li> -->
    <!-- <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

A python library that assists in debugging batch compute enviornments in AWS, GCP and Azure and Kubernetes. Currently only supports AWS Batch but this will be extended to include other cloud enviornment. 

Additionally currently assumes your compute enviornments in AWS batch were built using Seqera platform but a more standard debugging tool will eventually be implemented.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation

To use this library, just install the package via pip. 

```sh
pip install batch-debugging
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To start using this library, first set the enviornment variables for the platform and the token:

```sh 
export PLATFORM_TOKEN=
export PLATFORM_URL=
```

Then import the client for Seqera platform and initalize it:

```python 
from core.client import AuthenticatedPlatformClient

authenticated_client = AuthenticatedPlatformClient()

```

The only current usable class is the DebugAWSBatch class. Here is an example script:

```python

from core.debug_aws_batch import DebugAWSBatch
from core.client import AuthenticatedPlatformClient

authenticated_client = AuthenticatedPlatformClient()

def fetch_compute_enviornment_status(compute_enviornment_name: str) -> None
    compute_env_status = debug_aws_batch.get_compute_env_status(compute_enviornment_name)
    print(compute_env_status)
```

<!-- ### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
 -->

 ## Contact

Shahbaz Mahmood -  shahbazmahmooood@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>
