#!/usr/bin/env python3
import os

import aws_cdk as cdk

from geoip2.geoip2_stack import Geoip2Stack

app = cdk.App()

Geoip2Stack(
    app, 'Geoip2StackUSE1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

Geoip2Stack(
    app, 'Geoip2StackUSE2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

Geoip2Stack(
    app, 'Geoip2StackUSW2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

cdk.Tags.of(app).add('Alias','Extensions')
cdk.Tags.of(app).add('GitHub','https://github.com/4n6ir/geoip2.git')

app.synth()