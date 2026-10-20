# Product video update — 20 October 2026

User approved deployment of this batch after reviewing the corrected local preview.
Publish through the repository's existing GitHub Pages workflow.

- Feldspar uses the newly supplied video beside Technical Evidence. The earlier
  HEIC still is not used. Its H.264 MP4 is 1,796,525 bytes versus the original
  20,223,335 bytes (about 91% smaller); VP9 WebM is provided as a fallback.
- IMG_3350 is exclusive to Quartz (`quartz-sand-for-ceramics`). Its video and
  poster are absent from every other product page. Bentonite keeps its existing
  yard clip, with the requested long caption suffix removed; Feldspar keeps its
  dedicated IMG_3391 clip. Other core pages show technical documents without
  a video or an empty media column.
- Both occurrences of the old packing-plant photo are removed from every core
  product page. The five decorative carousel pages are unchanged. Non-product
  uses of the packing photo remain.
- New clips are upright 540×960 at 24fps, tone-mapped from phone HDR to SDR
  BT.709. Audio, data tracks and source camera/location metadata are stripped.
  Originals remain untouched. Encoders and private frame sheets stay in `tmp/`.
- Native controls, muted inline playback, no autoplay or looping, poster images
  and `preload="none"` keep the section quiet until the visitor chooses to play.
  MP4 comes first; portrait footage is contained, not cropped, at a bounded height.

Verification: four-point frame review of both new clips, complete decoding of
all four encoded files without errors, 88 local Python tests (including eight
pre-existing untracked tests), 81 JavaScript tests, and the site verifier for
40 routes and 27 technical documents pass. Product-media tests cover the
dedicated sources, removed photo/caption, audio-free MP4 track structure,
fast-start layout, local asset paths, and unchanged decorative pages.
An isolated clean-source production build also passes its 80 tracked/new Python
tests and the full artifact verifier. The local preview serves that artifact,
with HTTP 200 responses and `video/mp4` delivery for Feldspar's primary clip.

Rendered browser/mobile playback remains unverified because the saved localhost
browser denial is respected. No Google settings, indexing requests, inquiries,
schedules, or unrelated workspace files were changed.
