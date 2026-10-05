# Design tokens

Colours, type scale, spacing and corner radii shared by the web UI and the
Android app, so both look like one product. They arrive with the first client
screens (build-plan stage 5).

- One source file of tokens with light and dark values; each client generates
  its own form from it (CSS custom properties for the web, a Compose theme for
  Android).
- Colours meet WCAG AA contrast in both themes.
