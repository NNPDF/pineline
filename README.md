<p align="center">
  <a href="https://n3pdf.github.io/pineline/">
    <img alt="Pineline"
    src="./public/pineline.svg"
    height=350>
  </a>
</p>

# Pineline - high-energy theory predictions

To install the required node dependencies, run:

```sh
npm install
```

To launch the web server (for local development), run:

```sh
npm run dev
```

#### Connect to the website

When the server is running, to access the website is not sufficient to connect
the URL it outputs, e.g. https://localhost:3000, because the page is mounted on
a subdirectory (i.e. it is sufficient, but you will see a 404 page).
So, you just have to access the corresponding subdirectory, browsing to
something like:

https://localhost:3000/pineline

### Requirements

In order to run you need [Node.js](https://nodejs.org/en/), i.e. available in
most (if not all) Linux distribution through the system package manager, and for
MacOS with [Homebrew](https://brew.sh/) (name of the package can range from
`node` to 'nodejs').

About the Node package manager, the default one is `npm`, and it should just
work. But to have a better experience, and to leverage the lock file present, it
is suggested to use [`pnpm`](https://pnpm.io/) instead (installation
instructions on the website).
