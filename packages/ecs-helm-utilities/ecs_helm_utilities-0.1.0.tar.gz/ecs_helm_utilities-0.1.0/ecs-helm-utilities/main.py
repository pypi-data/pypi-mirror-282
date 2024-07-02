#!/usr/bin/env python
import click


@click.command()
@click.option('--generate-tag/--no-generate-tag', default=False, help="This generates a git tag from the chart's image.tag, appVersion, and version values")
def handle_args(generate_tag):
   
    if generate_tag:
        print("Generating tag...")

if __name__ == "__main__":  # pragma: no cover
    handle_args()

