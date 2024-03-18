# Facebook App Checker

A Python script to verify the validity of Facebook App credentials and check access to various functionalities.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Dependencies](#dependencies)
- [License](#license)

## Description

This script verifies the validity of Facebook App credentials (App ID and App Secret) by obtaining an access token and then checks access to various functionalities such as Ads Management, Page Management, and retrieving user information.

## Installation

1. Make sure you have Python installed on your system.
2. Install the requests and colorama libraries using pip:

    ```bash
    pip install requests colorama
    ```

## Usage

1. Run the script `facebook_checker.py` with your Facebook App ID and App Secret as command-line arguments:

    ```bash
    python facebook_checker.py app_id app_secret
    ```

Replace `app_id` and `app_secret` with your actual Facebook App ID and App Secret.

