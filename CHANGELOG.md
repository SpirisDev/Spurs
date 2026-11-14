# Changelog

All notable changes to Spurs Math are documented here.

## [0.2.1] - 2026-11-14

### Changed

- Updated the `MultiopBasic` class to accept positional arguments using `*args`.
- Changed multi-operation calls to use positional arguments rather than a list.

### API change

Previous usage:

```python
b.add([5, 6, 7, 9])
```

Updated usage:

```python
b.add(5, 6, 7, 9)
```

**Note:** The previous list-based calling convention is no longer supported by this interface.

## [0.2.0] - 2026-11-14

### Added

- Documentation
- Added README.md
- Added API.md

## [0.1.0]

### Initial development

- Initial version of Spurs Math.

---
