# CleanTreeFlow

Small Python utility for making AEM/JCR `.content.xml` structures easier to inspect during development.

It reads a local XML file, traverses the `service-providers` hierarchy, decodes selected node-name sequences such as `_x0020_`, and prints readable provider/category/product paths.

## Example

Input:

```xml
<service-providers>
  <Provider_x0020_A>
    <Internet_x0028_Hogar_x0029_>
      <Plan_x0035_G_x002b_ />
    </Internet_x0028_Hogar_x0029_>
  </Provider_x0020_A>
</service-providers>
```

Output:

```text
Provider A Internet(Hogar) Plan5G+
```

## Usage

Requires Python 3.10+ and no external dependencies.

```bash
git clone https://github.com/AndMad404/CleanTreeFlow.git
cd CleanTreeFlow
```

Place the XML file in the project root as:

```text
.content.xml
```

Then run:

```bash
python CleanTreeFlow.py
```

## How it works

`CleanTreeFlow.py`:

- Parses `.content.xml` with `xml.etree.ElementTree`.
- Finds the `service-providers` hierarchy.
- Extracts provider, category, and product node names.
- Decodes the supported `_xHHHH_` sequences.
- Prints the resulting paths to the terminal.

## Current limitations

The tool is intentionally specialized:

- It expects the `service-providers` structure.
- It currently reads only the first product under each category.
- It decodes a fixed set of character sequences.
- It does not modify XML files or connect to AEM.
- It does not automate AEM workflows.

## License

MIT. See [`LICENSE`](LICENSE).