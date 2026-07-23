# Recipe: Git LFS video delivery

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Explicit promotion | Human approved the exact review cut | Approval record | Human | Required |
| Singular final | One versioned file is copied into `deliverables/final/` | Delivery record | Editor | Required |
| Integrity | Promoted file hash equals the approved review-cut hash | SHA-256 output | Editor | Required |
| LFS rule | The final path matches a narrow `filter=lfs` attribute | `git check-attr` | Partner agent | Required |
| Pointer staging | Git index stores an LFS pointer, not MP4 bytes | Staged blob inspection | Partner agent | Required |
| Scope safety | Raw, generated, review, cache, and temporary media remain ignored | Staged path audit | Partner agent | Required |
| Remote verification | Commit and LFS object reach the intended remote branch | Push output and remote SHA | Partner agent | Required |

## Policy

Use this recipe only when the repository owner explicitly asks to version the final video. Do not
track all project media by default. Keep raw generations, review cuts, intermediate renders, audio
stems, caches, and downloaded sources outside Git unless a separate decision explicitly promotes
them.

## Steps

1. Identify the exact human-approved review cut and its delivery record.
2. Copy it byte-for-byte to a versioned path under `deliverables/final/`.
3. Compare SHA-256 hashes.
4. Add a narrow `.gitattributes` rule for the final directory or exact file.
5. Add a narrow `.gitignore` exception for only the promoted final.
6. Stage the final and confirm `git check-attr filter -- <path>` returns `lfs`.
7. Inspect `git show :<path>` and confirm it is a Git LFS pointer containing version, oid, and size.
8. Confirm no secret file, raw media, review cut, cache, or local archive is staged.
9. Commit and push without force.
10. Verify the remote branch SHA and a clean or understood local status.

## Failure handling

If LFS authentication or upload fails, do not bypass LFS or commit the MP4 as a regular Git blob.
Keep the commit locally, report the exact failure, and repair remote LFS authentication before
retrying the same push.
