import os
import logging

if 'LOG_LEVEL' in os.environ:
    numeric_level = getattr(logging, os.environ['LOG_LEVEL'].upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {os.environ["LOG_LEVEL"]}')
    logging.basicConfig(level=numeric_level)
else:
    logging.basicConfig()

logger = logging.getLogger(__name__)

with open('input.txt') as f:
    lines = f.read().splitlines()

SAFE_LEVELS = [1, 2, 3]

reports = []
for line in lines:
    reports.append([int(level) for level in line.split(' ')])

total_safe_reports = 0
for report in reports:
    logger.info('Processing report %s', report)
    safe = True
    if report[1] - report[0] < 0:
        decreasing_trend = True
    else:
        decreasing_trend = False

    for index in range(len(report) - 1):
        level_delta = report[index + 1] - report[index]
        if abs(level_delta) not in SAFE_LEVELS:
            logger.info('Unsafe due to non gradual change %s', abs(level_delta))
            safe = False
            break

        if level_delta < 0 and decreasing_trend is False:
            logger.info('Unsafe due to trend swap')
            safe = False
            break

        elif level_delta > 0 and decreasing_trend is True:
            logger.info('Unsafe due to trend swap')
            safe = False
            break

    if safe:
        logger.info('Safe report')
        total_safe_reports += 1

print(f'{total_safe_reports} reports are safe')
