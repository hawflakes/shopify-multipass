#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multipass import Multipass

m = Multipass('MULTIPASS SECRET GOES HERE')

customer = { "email": "test@example.com"}


token = m.generateToken(customer)

print(token)
