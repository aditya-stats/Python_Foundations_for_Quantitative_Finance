# Exploratory Statistical Analysis of Daily Stock Returns

## Overview

This project analyzes daily returns of Tata Steel using descriptive statistical tools. The goal is to understand the distributional and risk characteristics of returns rather than build predictive models.

## Method

1. Computed daily simple returns from closing prices

2. Calculated mean, volatility, skewness, kurtosis, and quantiles

3. Plotted return histogram

4. Examined 30-day rolling volatility

## Key Findings

Returns are centered around a small positive mean, but volatility is much larger than the average return.

The distribution is approximately symmetric.

High excess kurtosis indicates heavy tails and frequent extreme movements.

Quantiles show similar magnitudes of extreme gains and losses.

Rolling volatility reveals time-varying risk and clear volatility clustering.

# Learning Journey Context

This project was completed at the end of Week 2 of my Python learning journey. It focuses on applying fundamental Python concepts and core descriptive statistical methods to real financial data.

## Tools

Python, pandas, numpy, matplotlib, yfinance