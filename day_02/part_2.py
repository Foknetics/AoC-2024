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

reports = []
for line in lines:
    reports.append([int(level) for level in line.split(' ')])


SAFE_LEVELS = [1, 2, 3]


def validate_report(report):
    logger.info('Validating report %s', report)
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

    return safe


total_safe_reports = 0
for report in reports:
    logger.info('Processing report %s', report)
    if validate_report(report):
        logger.info('Safe with no dampener')
        total_safe_reports += 1
        continue

    for dampen_index in range(len(report)):
        alternative_report = report.copy()
        dampened_level = alternative_report.pop(dampen_index)
        logger.info('Testing dampening level %s: %s',
                    dampen_index, dampened_level)
        if validate_report(alternative_report):
            logger.info('Safe with dampener')
            total_safe_reports += 1
            break

print(f'{total_safe_reports} reports are safe')
