# Bentonite media and Marble Chips release — 20 October 2026

## Requested changes

- Bentonite's product image uses the user-supplied clay photo, with matching
  material-directory/related thumbnails and Product schema image. WebP copies
  provide 160, 480, 960 and 1000px choices without AI retouching or recolouring.
- The identified packing-plant photo occurred twice on the Bentonite page. Both
  occurrences are removed there; it is not deleted from other pages that use it.
  A single supplied yard clip appears beside the technical documents instead.
- Marble Chips is included with its twelve marble selections, five listed grades
  and clean carousel. The prior shared decorative-page polish/enquiry forms are
  included as its dependencies. Eleven core products and sixteen catalogue
  products remain, with forty canonical routes and fifty-seven carousel photos.

## Video processing and behavior

The original 848×480 clip is about 16 seconds and 3,092,093 bytes. Its content and
aspect ratio are retained, with web delivery at 24fps. No supplier/plant ownership,
test result or material performance is inferred from this footage.

- Primary: H.264 Main / yuv420p MP4, 866,210 bytes, about 72% smaller than source.
  Its `moov` box precedes `mdat` for fast-start playback.
- Fallback: VP9 WebM, 1,178,057 bytes, about 62% smaller than source.
- Both versions contain exactly one video stream and no audio stream. Audio was
  removed during encoding, not merely hidden behind a muted button.
- Native controls, `muted`, `playsinline`, `preload="none"`, a 39,260-byte poster,
  intrinsic dimensions and a short descriptive caption are used. There is no
  automatic playback or looping. Source ordering prefers the smaller MP4.
- Scoped `contain` fitting retains the full frame on desktop and small screens.
  Video and poster paths follow the existing GitHub-project-aware base handling.

Poster and source footage frames at 0, 5, 10 and 15 seconds were inspected.
The clip shows material stockpiles, a loader and a yard building. Captioning
describes it as a silent visual reference, not a grade or performance test.
Original user files remain untouched. Encoding tools, source paths, frame sheets
and private processing evidence remain in ignored `tmp/bentonite-media`, outside
the production artifact. CI needs only the finished media, not FFmpeg or Pillow.

References: [HTML video attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
and [FFmpeg container/fast-start documentation](https://ffmpeg.org/ffmpeg-formats.html).
`preload="none"` is a browser loading hint, not a guarantee of zero media requests.
Smaller files and source checks are not measured Core Web Vitals or a speed score.

## Verification boundaries

Check the clean exact-staged production build, image paths/dimensions, muted
video markup, source codecs, MP4 box/track structure, all decorative choices,
CAPTCHA and server-confirmed lead semantics. Decode both output clips to confirm
there are no decoder errors. After deployment, check live routes and media hashes,
MIME types and byte-range delivery without claiming rendered browser QA.

Saved localhost browser denial remains respected: no retry, alternate port,
remote rendering or PageSpeed workaround. Rendered mobile/playback behavior is
not independently verified. No real enquiry, Google setting change, indexing
submission, new schedule or unrelated workspace edit is part of this release.

Pre-release validation passed in an exact-staged clean checkout: 73 Python and
81 JavaScript tests, the production verifier for 40 pages and 27 documents,
whitespace checks, both full video decodes, and all seven new media hashes in the
artifact. Private preparation/runtime files and the supplier PDF are excluded.
Unrelated README/config/reporting edits and invoice deletions are not staged.
