#!/bin/sh

pytest --cov=src --cov-report term --cov-report html --cov-report xml:coverage.xml --junitxml report.xml .