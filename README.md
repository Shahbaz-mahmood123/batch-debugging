# Batch Debugging
<h3 align="center">batch_debugging</h3>

  <p align="center">
    A Python library crafted to simplify the debugging of batch compute environments across AWS, GCP, Azure, and Kubernetes.
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

A Python library designed to streamline the debugging of batch compute environments in AWS, GCP, Azure, and Kubernetes. Currently, it exclusively supports AWS Batch, with plans for future extensions to encompass other cloud environments. While presently tailored for compute environments built using the Seqera platform in AWS Batch, a more universal debugging tool is envisioned for future implementation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation

To use this library, just install the package via pip. 

```sh
pip install batch-debugging
```

<!-- GETTING STARTED -->
## Getting Started

### AWS
To start using this library for AWS, first set the enviornment variables for the provider you would like to use:
To use the aws fuctionality the below enviornment variable is needed:

```sh 
export AWS_REGION=$AWS_REGION
```
The relevant IAM permissions needed:
```
Coming soon
```
### GCP

To use the GCP functionality please set the below enviornment variables"

```sh 
export GCP_PROJECT_ID=$GCP_PROJECT_ID
export GCP_REGION=$GCP_REGION
```

The relevant IAM permissions needed:
```
Coming soon
```

### Azure

Usage guide Coming soon

The relevant IAM permissions needed:
```
Coming soon
```

### Seqera platform

To use the Seqera platform Fuctionality please set the below enviornemnt variables

```sh 
export PLATFORM_TOKEN=$PLATFORM_TOKEN
export PLATFORM_URL=$PLATFORM_URL
```

## Example script:

here is an example script using the DebugAWSBatch class:

```python

from core.debug_aws_batch import DebugAWSBatch

debug_aws_batch = DebugAWSBatch()

def fetch_compute_autoscaling_group_activity(compute_env_id: str) -> dict
    try:
      autoscaling_group = debug_aws_batch.get_autoscaling_group(compute_env_id)

      if autoscaling_group == None:
        return ["Could not fetch the autoscaling group"]

      autoscaling_activity = debug_aws_batch.get_scaling_activities(autoscaling_group)
      return autoscaling_activity

    except Exception as e:
      return ["An error occured retrieving the running and failed jobs"]
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
