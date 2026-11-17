# ValueFormattingConfigurationObjectBuilder

`VRage:Keen.VRage.Library.Utils.ValueFormattingConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Library.Utils`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Engine\Assets\Configurations\Setup\ValueFormattingConfiguration.def`

```json
{
  "Guid": "932915c0-1a52-497d-bd09-61074b3b5490",
  "Symbols": {
    "None": "UnitNone",
    "Meters": "UnitMeters",
    "MetersPerSecond": "UnitMetersPerSecond",
    "MetersPerSecondSquared": "UnitMetersPerSecondSquared",
    "CubicMeters": "UnitCubicMeters",
    "Liters": "UnitLiters",
    "LitersPerSecond": "UnitLitersPerSecond",
    "Radians": "UnitDegrees",
    "RadiansSecond": "UnitRadiansPerSecond",
    "RadiansPerSecond": "UnitRadiansSecond",
    "Degrees": "UnitDegrees",
    "DegreesPerSecond": "UnitDegreesPerSecond",
    "DegreesPerSecondSquared": "UnitDegreesPerSecondSquared",
    "RevolutionsPerMinute": "UnitPRM",
    "RightAngles": "UnitRightAngles",
    "Kilograms": "UnitMass",
    "KilogramsPerCubicMeters": "UnitKilogramsPerCubicMeters",
    "Newtons": "UnitNewtons",
    "NewtonsSecond": "UnitNewtonsSecond",
    "NewtonsMeter": "UnitNewtonsMeter",
    "Bytes": "UnitBytes",
    "Brightness": "UnitBrightness",
    "Hz": "UnitHertz",
    "GHz": "UnitGigahertz",
    "Pixels": "UnitPixels",
    "Seconds": "UnitSeconds",
    "Kilowatts": "UnitKilowatts",
    "KilowattHours": "UnitKilowattHours"
  },
  "MagnitudeSuffixes": {
    "None": [
      "UnitNone",
      "UnitNoneThousand",
      "UnitNoneMillion",
      "UnitNoneBillion"
    ],
    "Kilograms": [
      "UnitMass",
      "UnitMassTon",
      "UnitMassKiloTon",
      "UnitMassMegaTon"
    ],
    "KilowattHours": [
      "UnitKilowattHours",
      "UnitMegawattHours",
      "UnitGigawattHours"
    ],
    "Kilowatts": [
      "UnitKilowatts",
      "UnitMegawatts",
      "UnitGigawatts"
    ],
    "Meters": [
      "UnitMeters",
      "UnitKilometers"
    ]
  },
  "NoneLabel": "None",
  "BooleanNames": {
    "True": "BooleanTrue",
    "False": "BooleanFalse"
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ValueFormattingConfigurationObjectBuilder')
search_content('', type_contains='ValueFormattingConfigurationObjectBuilder')
```
