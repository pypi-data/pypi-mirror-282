# Posting.

Posting is an powerful HTTP client which brings Postman-like functionality to your terminal.

It's designed for those who prefer working in a terminal environment and enjoy fast, keyboard-centric user interfaces.

<img width="1332" alt="image" src="https://github.com/darrenburns/posting/assets/5740731/54b500df-48ac-4a8a-84ad-e5f64dbdc023">

It's still a work in progress and far from feature complete. Please don't open any bug reports yet - although I'm happy to hear ideas/suggestions!

## Installation

Posting can be installed via [`pipx`](https://pipx.pypa.io/stable/):

```bash
pipx install posting
```

Python 3.11 or later is required.

More installation methods (`brew`, etc) will be added soon.

## Collections

Requests can be stored inside "collections" on your file system.
A collection is simply a directory containing one or more requests.

Each request is stored as a simple YAML file, suffixed with `.posting.yaml` - easy to read, understand, and version control!

Here's a quick example of a `*.posting.yaml` file.

```yaml
name: Create user
description: Adds a new user to the system.
method: POST
url: https://jsonplaceholder.typicode.com/users
body: |-
  {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com"
  }
headers:
- name: Content-Type
  value: application/json
- name: Some-Header
  value: Some value
  enabled: false
params:
- name: sendWelcomeEmail
  value: 'true'
```

To open a collection, simply pass the path to the `--collection` option when launching Posting:

```bash
posting --collection path/to/collection
```

The supplied directory will be recursively searched for files matching `**/*.posting.yaml`, and they'll appear in the sidebar.

If you don't supply a collection directory, the current working directory will be used.

To save the currently open request, press <kbd>ctrl</kbd>+<kbd>s</kbd>.

## Navigation

Posting can be navigated using either mouse or keyboard.

### Jump mode

Jump mode is the fastest way to get around in Posting.

Press <kbd>ctrl</kbd>+<kbd>o</kbd> to enter jump mode.

A key overlay will appear on the screen, allowing you to jump to any widget by pressing the corresponding key.

https://github.com/darrenburns/posting/assets/5740731/5e7cdf57-90b2-4dba-b468-0057c6ef1806

### Tab navigation

<kbd>tab</kbd> and <kbd>shift+tab</kbd> will move focus between widgets,
and <kbd>j</kbd>/<kbd>k</kbd> will move around within a widget.

### Keyboard shortcuts

Important keyboard shortcuts are displayed at the bottom of the screen.

However, there are many other shortcuts available - these will be documented soon.

<!-- TODO - document other shortcuts. -->

## Command palette

Some functionality in Posting doesn't warrant a dedicated keyboard shortcut (for example, switching to a specific theme), and can instead be accessed via the _command palette_.

To open the command palette, press <kbd>ctrl</kbd>+<kbd>p</kbd>.

https://github.com/darrenburns/posting/assets/5740731/a199e5f2-5621-42e6-b239-a796d1dc144a

## Animation

You can turn off animations by setting the environment variable `TEXTUAL_ANIMATIONS=none`.

## Planned Features

- **Keyboard Friendly**: Navigate and iterate on your APIs using simple keyboard shortcuts.
- **File System Storage**: Your collections are saved as files, meaning you can easily sync them using version control or your favorite cloud provider.
- **Multiplatform**: Run on MacOS, Linux and Windows.
- **Template Variables**: Define variables and substitute them into your requests.
- **Powerful Text and JSON Editor**: Offers tree-sitter powered syntax highlighting, undo/redo, copy/paste, and more.
- **Runs Over SSH**: Send requests from a remote host via SSH.
- **Your Idea Here**: Please let me know if you have opinions on the features above, or any other ideas!
