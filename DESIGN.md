---
version: alpha
name: EmpathoAI Sovereign Precision
description: Human depth and machine leverage expressed through a precise, editorial, telemetry-led visual system.
colors:
  primary: "#0A0A0B"
  canvas: "#0A0A0B"
  surfaceDeep: "#141416"
  surfaceMid: "#1E1E22"
  hairline: "#2D2D2F"
  ivory: "#F5F5F5"
  body: "#C7C7CC"
  muted: "#8E8E93"
  orange: "#FF4402"
  lightCanvas: "#FFFFFF"
  lightBody: "#0A0A0B"
  lightMuted: "#666668"
typography:
  display:
    fontFamily: IBM Plex Sans
    fontSize: 4rem
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  heading:
    fontFamily: IBM Plex Sans
    fontSize: 2.25rem
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  subheading:
    fontFamily: IBM Plex Sans
    fontSize: 1.375rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0em"
  body:
    fontFamily: IBM Plex Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"
  telemetry:
    fontFamily: IBM Plex Mono
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.05em"
rounded:
  none: 0px
spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
components:
  primary-action:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.telemetry}"
    rounded: "{rounded.none}"
    padding: 16px
  secondary-action:
    backgroundColor: "{colors.surfaceDeep}"
    textColor: "{colors.ivory}"
    typography: "{typography.telemetry}"
    rounded: "{rounded.none}"
    padding: 16px
  dark-surface:
    backgroundColor: "{colors.surfaceDeep}"
    textColor: "{colors.ivory}"
    rounded: "{rounded.none}"
    padding: 24px
  light-surface:
    backgroundColor: "{colors.lightCanvas}"
    textColor: "{colors.lightBody}"
    rounded: "{rounded.none}"
    padding: 24px
  signal-marker:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    size: 64px
  body-copy:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body}"
  telemetry-label:
    backgroundColor: "{colors.surfaceMid}"
    textColor: "{colors.muted}"
    typography: "{typography.telemetry}"
  structural-rule:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ivory}"
    size: 1px
  light-metadata:
    backgroundColor: "{colors.lightCanvas}"
    textColor: "{colors.lightMuted}"
    typography: "{typography.telemetry}"
---

## Overview

EmpathoAI's visual language is human-first, compliance-first, and precision-oriented. It combines editorial clarity with technical telemetry. The system is designed to make signals, friction, decisions, and interventions legible rather than decorative.

The thesis is **HUMAN DEPTH. MACHINE LEVERAGE.** The visual antagonist is disorder that has been scaled before its foundations were corrected.

## Colors

- **Obsidian Dark (`#0A0A0B`):** Default canvas for owned interfaces, dashboards, internal tools, and controlled digital experiences.
- **Deep Surface (`#141416`):** Secondary surfaces, code blocks, and grouped modules.
- **Mid Surface (`#1E1E22`):** Hover states, active structural surfaces, and dividers where needed.
- **Technical Hairline (`#2D2D2F`):** Crisp one-pixel structural boundaries.
- **Technical Ivory (`#F5F5F5`):** Primary light text and headlines on dark surfaces.
- **Body (`#C7C7CC`):** Comfortable secondary body text on dark surfaces.
- **Muted Telemetry (`#8E8E93`):** Metadata, timestamps, captions, and secondary metrics.
- **Electric Signal Orange (`#FF4402`):** Intervention signal, active coordinates, and important calls to action. Use sparingly, approximately 2–4% of a surface. It never decorates.

For external documents and reading-heavy experiences, use the defined light tokens while preserving the same signal orange and structural precision.

## Typography

Use IBM Plex Sans for editorial content and IBM Plex Mono for telemetry, metrics, code, labels, and machine-readable data. Type hierarchy should be clear, restrained, and information-dense without becoming cramped.

## Layout

Use disciplined negative space, an architectural grid, and strong alignment. Prefer a small number of meaningful regions over nested containers. Make diagrams, telemetry, and decision-relevant information prominent. The intended visual distribution is approximately 70% diagrams and telemetry, 20% authentic editorial photography, and 10% conceptual plates when imagery is relevant.

## Elevation & Depth

Avoid decorative shadows and excessive layering. Depth comes from canvas changes, hairline borders, spacing, and signal placement. A surface should earn its separation from surrounding content.

## Shapes

Use `0px` border radius as the default across modules, cards, controls, markers, and containers. Use crisp `1px` hairlines for structural boundaries.

## Components

- Use one primary intervention signal per region where possible.
- Keep actions explicit and telemetry-like.
- Use the signal marker as a precise coordinate, not an ornamental icon tile.
- Preserve sufficient contrast and a readable focus state in both dark and light systems.

## Do's and Don'ts

### Do

- Build hierarchy through typography, spacing, and evidence.
- Use orange only to mark significance or intervention.
- Keep interfaces calm, precise, and operationally legible.
- Validate responsive behavior and WCAG contrast before shipping.
- Preserve the dark system for owned digital tools and the light system for reading and printing.

### Don't

- Do not use gradients as decoration.
- Do not use rounded-square icon tiles or nested card stacks by default.
- Do not use gray text on colored backgrounds when contrast is insufficient.
- Do not use pure black or uncontrolled gray in place of the defined tokens.
- Do not make every element visually loud.
