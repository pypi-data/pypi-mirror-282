#!/usr/bin/env python
import click
import yaml

@click.command()
@click.option('--generate-tag/--no-generate-tag', default=False, help="This generates a git tag from the chart's image.tag, appVersion, and version values")
def handle_args(generate_tag):
   
    if generate_tag:
        print("Generating tag...")
        with open('values.yaml') as values_file:
            values = yaml.safe_load(values_file)
        image_tag = values['image']['tag']
        with open('Chart.yaml') as chart_file:
            chart_values = yaml.safe_load(chart_file)
        version = chart_values['version']
        app_version = chart_values['appVersion']
        tag="%s;%s;%s" % (app_version, image_tag, version)
        print(tag)

if __name__ == "__main__": 
    handle_args()

