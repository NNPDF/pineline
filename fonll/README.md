# FONLL studies

FONLL is the most complex pineline procedure, since it involves an *advanced*
integration of the various tools, beyond the usual pipeline.

To get started run:

```sh
./bootstrap workspace
```


## Scripts

Since the configuration itself is non-trivial, a few scripts are provided to
speed up the setup of an environment suitable for these studies.

- `bootstrap`: create a whole workspace
  - creates a virtualenv
  - downloads relevant PDF sets
  - installs LHAPDF
  - copies all the relevant scripts
  - usage:
- `activate`: activate the environment and export convenient variables
- `deact`: deactivate the environment and reset the variables
- `switch`: switch between numerical and analytical FONLL
- `update`: update the copy of the scripts
- `numerical`/`analytical`: run the two FONLL calculations
- `compare`: generate suitable plots

### Usage

Once run the `bootstrap` as described above, enter the environment sourcing the
copy of the `activate` script in the workspace:

```sh
# inside `workspace`
. ./activate
```

After that, the workspace itself gets added to the `$PATH`, and convenient
aliases are exported, so you could use all of the following:
```sh
# switch to numerical FONLL
switch n
# switch to analytical FONLL
switch a

# deactivate the environment
deact

# update the environment with bootstrap
bootstrap /path/to/workspace
# or (within the workspace)
bootstrap .

# run numerical FONLL
numerical /path/to/workspace
# or (within the workspace)
numerical
# same for `analytical`

# just fetch a new copy of the scripts
update
```
