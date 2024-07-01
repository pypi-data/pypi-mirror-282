# Copyright 2022 mdavid217
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Set, cast

from rp2.abstract_country import AbstractCountry
from rp2.computed_data import ComputedData
from rp2.in_transaction import InTransaction
from rp2.localization import _
from rp2.logger import create_logger
from rp2.plugin.report.abstract_ods_generator import AbstractODSGenerator
from rp2.rp2_decimal import ZERO, RP2Decimal
from rp2.rp2_error import RP2TypeError

LOGGER: logging.Logger = create_logger("open_positions")

_TEMPLATE_SHEETS: Set[str] = {"Asset", "Asset - Exchange", "Input"}
_TEMPLATE_SHEETS_TO_KEEP: Set[str] = {"__" + sheet_name for sheet_name in _TEMPLATE_SHEETS}
_FIAT_UNIT_DATA_STYLE_2_DECIMAL_MINIMUM = RP2Decimal("1")
_FIAT_UNIT_DATA_STYLE_4_DECIMAL_MINIMUM = RP2Decimal("0.20")

_ASSET: str = "Asset"
_ASSET_EXCHANGE: str = "Asset - Exchange"
_INPUT: str = "Input"
_INPUT_VALUE_STRING: str = "Enter asset value"
_REPORT_INPUT_VALUE_STRING: str = "See Input tab"


class Generator(AbstractODSGenerator):
    OUTPUT_FILE: str = "open_positions.ods"
    HEADER_ROWS = 3

    __legend: List[List[str]] = []
    __asset_header_names_row_1: List[str] = []
    __asset_header_names_row_2: List[str] = []
    __asset_exchange_header_names_row_1: List[str] = []
    __asset_exchange_header_names_row_2: List[str] = []
    __input_header_names_row_1: List[str] = []
    __input_header_names_row_2: List[str] = []

    # pylint: disable=line-too-long
    def _setup_text_data(self, country: AbstractCountry) -> None:
        currency_code: str = country.currency_iso_code.upper()

        self.__legend: List[List[str]] = [
            # fmt: off
            [_("Open Positions / Unrealized Gains")],
            [_("Fill in Asset Prices in the Input Tab for calculations")],
            [_("This report leverages the details of your transactions to give you a snapshot of the value of your unsold holdings")],
            [_("This file contains two versions of the same report. One version is grouped by Asset, the other by Asset and Exchange (or wallet)")],
            [""],
            [_("General")],
            [_("Accounting Method")],
            [_("From Date Filter")],
            [_("To Date Filter")],
            [""],
            [_("Report Fields")],
            [_("Asset"), _("Crypto / asset symbol")],
            [_("Holder"), _("Asset holder")],
            [_("Exchange"), _("Exchange or wallet where balance is held (Asset - Exchange tab only)")],
            [_("Crypto Balance"), _("Amount of given asset held")],
            [_("{} Per Unit Cost Basis").format(currency_code), _("Sum of fiat cost to acquire the balance of crypto based on in-flow transactions divided by the crypto balance")],
            [_("{} Unrealized Cost Basis").format(currency_code), _("Sum of fiat cost to acquire the balance of crypto based on in-flow transactions")],
            [_("Cost Basis Weight %"), _("Size of investment relative to other assets for cost basis ({} Unrealized Cost Basis divided by the sum of all assets' {} Unrealized Cost Basis)").format(currency_code, currency_code)],
            [_("{} Per Unit Input Price").format(currency_code), _("Looked up from the Input tab for the given asset")],
            [_("{} Unrealized Value").format(currency_code), _("Crypto Balance * Input Price")],
            [_("{} Unrealized Gain / Loss").format(currency_code), _("Unrealized Value - Unrealized Cost Basis")],
            [_("{} Unrealized Gain / Loss %").format(currency_code), _("Percent change between Unrealized Value and Unrealized Cost Basis")],
            [_("Unrealized G/L of Total Cost Basis %"), _("Indicates the percent of which this asset's unrealized gain/loss contributed to the whole portfolio's Unrealized Gain / Loss % (Gain/Loss relative to total cash investment)")],
            [_("{} Unrealized Value Weight %").format(currency_code), _("Size of investment relative to the portfolio's unrealized value (Unrealized Value divided by sum of all assets' Unrealized Values)")],
            [""],
            [_("Color Code")],
            [_("Gray"), _("Information from transactions")],
            [_("Yellow"), _("Information calculated based on values entered in the Input tab")],
            # fmt: on
        ]

        self.__asset_header_names_row_1: List[str] = [
            "",
            "",
            _("Crypto"),
            _("{} Per Unit").format(currency_code),
            _("{} Unrealized").format(currency_code),
            _("Cost Basis"),
            _("{} Per Unit").format(currency_code),
            _("{} Unrealized").format(currency_code),
            _("{} Unrealized").format(currency_code),
            _("{} Unrealized").format(currency_code),
            _("Unrealized G/L of"),
            _("{} Unrealized").format(currency_code),
        ]

        self.__asset_header_names_row_2: List[str] = [
            _("Asset"),
            _("Holder"),
            _("Balance"),
            _("Cost Basis"),
            _("Cost Basis"),
            _("Weight %"),
            _("Input Price"),
            _("Value"),
            _("Gain / Loss"),
            _("Gain / Loss %"),
            _("Total Cost Basis %"),
            _("Value Weight %"),
        ]

        self.__asset_exchange_header_names_row_1: List[str] = [
            "",
            "",
            "",
            _("Crypto"),
            _("{} Per Unit").format(currency_code),
            _("{} Unrealized").format(currency_code),
            _("Cost Basis"),
            _("{} Per Unit").format(currency_code),
            _("{} Unrealized").format(currency_code),
            _("{} Unrealized").format(currency_code),
            _("{} Unrealized").format(currency_code),
            _("Unrealized G/L of"),
            _("{} Unrealized").format(currency_code),
        ]

        self.__asset_exchange_header_names_row_2: List[str] = [
            _("Asset"),
            _("Holder"),
            _("Exchange"),
            _("Balance"),
            _("Cost Basis"),
            _("Cost Basis"),
            _("Weight %"),
            _("Input Price"),
            _("Value"),
            _("Gain / Loss"),
            _("Gain / Loss %"),
            _("Total Cost Basis %"),
            _("Value Weight %"),
        ]

        self.__input_header_names_row_1: List[str] = [
            _("Crypto"),
            "",
        ]

        self.__input_header_names_row_2: List[str] = [
            _("Asset"),
            _("Price"),
        ]

    def generate(
        self,
        country: AbstractCountry,
        years_2_accounting_method_names: Dict[int, str],
        asset_to_computed_data: Dict[str, ComputedData],
        output_dir_path: str,
        output_file_prefix: str,
        from_date: date,
        to_date: date,
        generation_language: str,
    ) -> None:
        # pylint: disable=too-many-branches

        if not isinstance(asset_to_computed_data, Dict):
            raise RP2TypeError(f"Parameter 'asset_to_computed_data' has non-Dict value {asset_to_computed_data}")

        self._setup_text_data(country)

        template_path: str = self._get_template_path("open_positions", country, generation_language)

        output_file: Any
        output_file = self._initialize_output_file(
            country=country,
            legend_data=self.__legend,
            years_2_accounting_method_names=years_2_accounting_method_names,
            output_dir_path=output_dir_path,
            output_file_prefix=output_file_prefix,
            output_file_name=self.OUTPUT_FILE,
            template_path=template_path,
            template_sheets_to_keep=_TEMPLATE_SHEETS_TO_KEEP,
            from_date=from_date,
            to_date=to_date,
        )

        asset: str
        computed_data: ComputedData

        asset_sheet = output_file.sheets[_ASSET]
        asset_exchange_sheet = output_file.sheets[_ASSET_EXCHANGE]
        input_sheet = output_file.sheets[_INPUT]

        self._fill_header(_("Open Positions by Asset"), self.__asset_header_names_row_1, self.__asset_header_names_row_2, asset_sheet, 0, 0, apply_style=False)
        self._fill_cell(asset_sheet, 0, 6, _("ENTER PRICES ON INPUT TAB"), apply_style=False)

        self._fill_header(
            _("Open Positions by Asset and Exchange"),
            self.__asset_exchange_header_names_row_1,
            self.__asset_exchange_header_names_row_2,
            asset_exchange_sheet,
            0,
            0,
            apply_style=False,
        )
        self._fill_cell(asset_exchange_sheet, 0, 7, _("ENTER PRICES ON INPUT TAB"), apply_style=False)

        self._fill_header(_("Asset Price Lookup Table"), self.__input_header_names_row_1, self.__input_header_names_row_2, input_sheet, 0, 0, apply_style=False)

        row_indexes: Dict[str, int] = {sheet_name: self.HEADER_ROWS for sheet_name in _TEMPLATE_SHEETS}

        # First loop - primary data collection
        #  - total_cost_basis: total cost basis for all transactions and all assets
        #  - asset_cost_bases: total cost basis for all transactions by asset
        #  - holders: list of holders with non-zero balances.
        #  - asset_crypto_balance_holder: sum of crypto balance for each asset by holder
        #  - asset_crypto_balance_holder_exchange: sum of crypto balance for each asset by holder and exchange
        total_cost_basis = ZERO
        asset_cost_bases: Dict[str, RP2Decimal] = {}
        holders: List[str] = []
        asset_crypto_balance_holder: Dict[str, Dict[str, RP2Decimal]] = {}
        asset_crypto_balance_holder_exchange: Dict[str, Dict[str, Dict[str, RP2Decimal]]] = {}

        for asset, computed_data in asset_to_computed_data.items():
            if not isinstance(asset, str):
                raise RP2TypeError(f"Parameter 'asset' has non-string value {asset}")
            ComputedData.type_check("computed_data", computed_data)

            # process in-flow transactions to collect the fiat cost basis data.
            for current_transaction in computed_data.in_transaction_set:
                in_transaction = cast(InTransaction, current_transaction)
                sold_percent: RP2Decimal = computed_data.get_in_lot_sold_percentage(in_transaction)
                transaction_cost_basis: RP2Decimal = in_transaction.fiat_in_with_fee * (RP2Decimal("1") - sold_percent)

                if transaction_cost_basis > ZERO:
                    value = asset_cost_bases.setdefault(asset, ZERO)
                    value += transaction_cost_basis
                    asset_cost_bases[asset] = value

                    total_cost_basis += transaction_cost_basis

            # process balance set data for the asset to collect holder and crypto balance data.
            for balance_set in computed_data.balance_set:
                if balance_set.final_balance > ZERO:
                    if balance_set.holder not in holders:
                        holders.append(balance_set.holder)

                    if asset not in asset_crypto_balance_holder:
                        asset_crypto_balance_holder[asset] = {}
                        asset_crypto_balance_holder_exchange[asset] = {}

                    if balance_set.holder not in asset_crypto_balance_holder[asset]:
                        asset_crypto_balance_holder[asset][balance_set.holder] = ZERO
                        asset_crypto_balance_holder_exchange[asset][balance_set.holder] = {}

                    asset_crypto_balance_holder[asset][balance_set.holder] += balance_set.final_balance

                    if balance_set.exchange not in asset_crypto_balance_holder_exchange[asset][balance_set.holder]:
                        asset_crypto_balance_holder_exchange[asset][balance_set.holder][balance_set.exchange] = balance_set.final_balance

        # Now looping through the assets to do the reporting.
        for asset, asset_cost_basis in asset_cost_bases.items():
            total_crypto_balance = ZERO
            for crypto_balance in asset_crypto_balance_holder[asset].values():
                total_crypto_balance += crypto_balance

            unit_cost_basis: RP2Decimal = asset_cost_basis / total_crypto_balance

            # For report clarity, change how much precision is displayed in the output based on the unit price. The raw value is
            # included in the output, so if the user desires they can change the cell format in the resulting file.
            # The default windowing is set up to hopefully give a good user experience for high value cryptos like BTC
            # all the way through cryptos with minute unit values like SHIB.
            unit_data_style: str = "fiat"
            if _FIAT_UNIT_DATA_STYLE_4_DECIMAL_MINIMUM <= unit_cost_basis < _FIAT_UNIT_DATA_STYLE_2_DECIMAL_MINIMUM:
                unit_data_style = "fiat_unit_4"
            elif unit_cost_basis < _FIAT_UNIT_DATA_STYLE_4_DECIMAL_MINIMUM:
                unit_data_style = "fiat_unit_7"

            # Add this asset to the Input sheet where the user will enter pricing value for the calculations
            input_sheet.append_rows(1)
            input_row_index: int = row_indexes[_INPUT]
            self._fill_cell(input_sheet, input_row_index, 0, asset)
            self._fill_cell(input_sheet, input_row_index, 1, _INPUT_VALUE_STRING, data_style="fiat_unit_7")
            row_indexes[_INPUT] = input_row_index + 1

            _vlookup_formula: str = ""
            _lookup_field: str = ""

            # Complete the asset table.
            for holder, holder_crypto_balance in asset_crypto_balance_holder[asset].items():
                holder_cost_basis: RP2Decimal = holder_crypto_balance * unit_cost_basis

                asset_sheet.append_rows(1)
                asset_row_index: int = row_indexes[_ASSET]
                _vlookup_formula = f"VLOOKUP(A{asset_row_index+1};${_('Input')}.A:B;2;0)"
                _lookup_field = f'=IF({_vlookup_formula}="{_INPUT_VALUE_STRING}";"{_REPORT_INPUT_VALUE_STRING}";{_vlookup_formula}'

                self._fill_cell(asset_sheet, asset_row_index, 0, asset)
                self._fill_cell(asset_sheet, asset_row_index, 1, holder)
                self._fill_cell(asset_sheet, asset_row_index, 2, holder_crypto_balance, data_style="crypto")
                self._fill_cell(asset_sheet, asset_row_index, 3, unit_cost_basis, data_style=unit_data_style)
                self._fill_cell(asset_sheet, asset_row_index, 4, holder_cost_basis, data_style="fiat")
                self._fill_cell(asset_sheet, asset_row_index, 5, holder_cost_basis / total_cost_basis, data_style="percent")
                self._fill_cell(asset_sheet, asset_row_index, 6, _lookup_field, data_style=unit_data_style)
                self._fill_cell(asset_sheet, asset_row_index, 7, f"=C{asset_row_index+1}*G{asset_row_index+1}", data_style="fiat")
                self._fill_cell(asset_sheet, asset_row_index, 8, f"=H{asset_row_index+1}-E{asset_row_index+1}", data_style="fiat")
                self._fill_cell(asset_sheet, asset_row_index, 9, f"=(H{asset_row_index+1}-E{asset_row_index+1})/E{asset_row_index+1}", data_style="percent")
                row_indexes[_ASSET] = asset_row_index + 1

            # Generate the Asset/Exchange table which will calc vals that will feed the asset table.
            for holder, exchanges in asset_crypto_balance_holder_exchange[asset].items():
                for exchange, crypto_exchange_balance in exchanges.items():
                    exchange_cost_basis: RP2Decimal = crypto_exchange_balance * unit_cost_basis

                    asset_exchange_sheet.append_rows(1)
                    asset_exchange_row_index: int = row_indexes[_ASSET_EXCHANGE]
                    _vlookup_formula = f"VLOOKUP(A{asset_exchange_row_index+1};${_('Input')}.A:B;2;0)"
                    _lookup_field = f'=IF({_vlookup_formula}="{_INPUT_VALUE_STRING}";"{_REPORT_INPUT_VALUE_STRING}";{_vlookup_formula}'

                    self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 0, asset)
                    self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 1, holder)
                    self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 2, exchange)
                    self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 3, crypto_exchange_balance, data_style="crypto")
                    self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 4, unit_cost_basis, data_style=unit_data_style)
                    self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 5, exchange_cost_basis, data_style="fiat")
                    self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 6, exchange_cost_basis / total_cost_basis, data_style="percent")
                    self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 7, _lookup_field, data_style=unit_data_style)
                    self._fill_cell(
                        asset_exchange_sheet, asset_exchange_row_index, 8, f"=D{asset_exchange_row_index+1}*H{asset_exchange_row_index+1}", data_style="fiat"
                    )
                    self._fill_cell(
                        asset_exchange_sheet, asset_exchange_row_index, 9, f"=I{asset_exchange_row_index+1}-F{asset_exchange_row_index+1}", data_style="fiat"
                    )
                    self._fill_cell(
                        asset_exchange_sheet,
                        asset_exchange_row_index,
                        10,
                        f"=(I{asset_exchange_row_index+1}-F{asset_exchange_row_index+1})/F{asset_exchange_row_index+1}",
                        data_style="percent",
                    )
                    row_indexes[_ASSET_EXCHANGE] = asset_exchange_row_index + 1

        # There are several portfolio-wide fields in the output that are dependent on values the user enters into the Input tab for
        # live calculation that cannot be accounted for in this report. Since I want to include a totals row in the output, I cannot do
        # full-column sums, e.g. =G4/SUM(G:G), so instead I am using the row index and the header rows info to scope the SUM to the
        # actual rows I know I have placed data into.

        asset_row_index = row_indexes[_ASSET]
        for row_idx in range(self.HEADER_ROWS, row_indexes[_ASSET]):
            self._fill_cell(asset_sheet, row_idx, 10, f"=I{row_idx+1}/SUM(E${self.HEADER_ROWS+1}:E${asset_row_index})", data_style="percent")
            self._fill_cell(asset_sheet, row_idx, 11, f"=H{row_idx+1}/SUM(H${self.HEADER_ROWS+1}:H${asset_row_index})", data_style="percent")

        asset_exchange_row_index = row_indexes[_ASSET_EXCHANGE]
        for row_idx in range(self.HEADER_ROWS, row_indexes[_ASSET_EXCHANGE]):
            self._fill_cell(asset_exchange_sheet, row_idx, 11, f"=J{row_idx+1}/SUM(F${self.HEADER_ROWS+1}:F${asset_exchange_row_index})", data_style="percent")
            self._fill_cell(asset_exchange_sheet, row_idx, 12, f"=I{row_idx+1}/SUM(I${self.HEADER_ROWS+1}:I${asset_exchange_row_index})", data_style="percent")

        # Save the last row index containing data so multiple total rows can be added.
        last_data_row_indexes = row_indexes.copy()

        # Asset sheet totals.
        if len(holders) > 1:
            for holder in holders:
                asset_sheet.append_rows(1)
                asset_row_index = row_indexes[_ASSET]
                last_data_index = last_data_row_indexes[_ASSET]
                self._fill_cell(asset_sheet, asset_row_index, 0, _("Total"), visual_style="bold_border")
                self._fill_cell(asset_sheet, asset_row_index, 1, holder, visual_style="bold_border")
                self._fill_cell(asset_sheet, asset_row_index, 2, "", visual_style="bold_border")
                self._fill_cell(asset_sheet, asset_row_index, 3, "", visual_style="bold_border")
                self._fill_cell(
                    asset_sheet,
                    asset_row_index,
                    4,
                    f'=SUMIF(B${self.HEADER_ROWS+1}:B${last_data_index};"{holder}";E${self.HEADER_ROWS+1}:E${last_data_index})',
                    visual_style="bold_border",
                    data_style="fiat",
                )
                self._fill_cell(asset_sheet, asset_row_index, 5, "", visual_style="bold_border")
                self._fill_cell(asset_sheet, asset_row_index, 6, "", visual_style="bold_border")
                self._fill_cell(
                    asset_sheet,
                    asset_row_index,
                    7,
                    f'=SUMIF(B${self.HEADER_ROWS+1}:B${last_data_index};"{holder}";H${self.HEADER_ROWS+1}:H${last_data_index})',
                    visual_style="bold_border",
                    data_style="fiat",
                )
                self._fill_cell(
                    asset_sheet,
                    asset_row_index,
                    8,
                    f'=SUMIF(B${self.HEADER_ROWS+1}:B${last_data_index};"{holder}";I${self.HEADER_ROWS+1}:I${last_data_index})',
                    visual_style="bold_border",
                    data_style="fiat",
                )
                self._fill_cell(
                    asset_sheet,
                    asset_row_index,
                    9,
                    f"=(H{asset_row_index+1}-E{asset_row_index+1})/E{asset_row_index+1}",
                    visual_style="bold_border",
                    data_style="percent",
                )
                self._fill_cell(asset_sheet, asset_row_index, 10, "", visual_style="bold_border")
                self._fill_cell(asset_sheet, asset_row_index, 11, "", visual_style="bold_border")
                row_indexes[_ASSET] = asset_row_index + 1

        asset_sheet.append_rows(1)
        asset_row_index = row_indexes[_ASSET]
        last_data_index = last_data_row_indexes[_ASSET]
        self._fill_cell(asset_sheet, asset_row_index, 0, _("Grand Total"), visual_style="bold_border")
        self._fill_cell(asset_sheet, asset_row_index, 1, "", visual_style="bold_border")
        self._fill_cell(asset_sheet, asset_row_index, 2, "", visual_style="bold_border")
        self._fill_cell(asset_sheet, asset_row_index, 3, "", visual_style="bold_border")
        self._fill_cell(asset_sheet, asset_row_index, 4, f"=SUM(E${self.HEADER_ROWS+1}:E${last_data_index})", visual_style="bold_border", data_style="fiat")
        self._fill_cell(asset_sheet, asset_row_index, 5, "", visual_style="bold_border")
        self._fill_cell(asset_sheet, asset_row_index, 6, "", visual_style="bold_border")
        self._fill_cell(asset_sheet, asset_row_index, 7, f"=SUM(H${self.HEADER_ROWS+1}:H${last_data_index})", visual_style="bold_border", data_style="fiat")
        self._fill_cell(asset_sheet, asset_row_index, 8, f"=SUM(I${self.HEADER_ROWS+1}:I${last_data_index})", visual_style="bold_border", data_style="fiat")
        self._fill_cell(
            asset_sheet,
            asset_row_index,
            9,
            f"=(H{asset_row_index+1}-E{asset_row_index+1})/E{asset_row_index+1}",
            visual_style="bold_border",
            data_style="percent",
        )
        self._fill_cell(asset_sheet, asset_row_index, 10, "", visual_style="bold_border")
        self._fill_cell(asset_sheet, asset_row_index, 11, "", visual_style="bold_border")
        row_indexes[_ASSET] = asset_row_index + 1

        # Asset - Exchange sheet totals.
        if len(holders) > 1:
            for holder in holders:
                asset_exchange_sheet.append_rows(1)
                asset_exchange_row_index = row_indexes[_ASSET_EXCHANGE]
                last_data_index = last_data_row_indexes[_ASSET_EXCHANGE]
                self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 0, _("Total"), visual_style="bold_border")
                self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 1, holder, visual_style="bold_border")
                self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 2, "", visual_style="bold_border")
                self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 3, "", visual_style="bold_border")
                self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 4, "", visual_style="bold_border")
                self._fill_cell(
                    asset_exchange_sheet,
                    asset_exchange_row_index,
                    5,
                    f'=SUMIF(B${self.HEADER_ROWS+1}:B${last_data_index};"{holder}";F${self.HEADER_ROWS+1}:F${last_data_index})',
                    visual_style="bold_border",
                    data_style="fiat",
                )
                self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 6, "", visual_style="bold_border")
                self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 7, "", visual_style="bold_border")
                self._fill_cell(
                    asset_exchange_sheet,
                    asset_exchange_row_index,
                    8,
                    f'=SUMIF(B${self.HEADER_ROWS+1}:B${last_data_index};"{holder}";I${self.HEADER_ROWS+1}:I${last_data_index})',
                    visual_style="bold_border",
                    data_style="fiat",
                )
                self._fill_cell(
                    asset_exchange_sheet,
                    asset_exchange_row_index,
                    9,
                    f'=SUMIF(B${self.HEADER_ROWS+1}:B${last_data_index};"{holder}";J${self.HEADER_ROWS+1}:J${last_data_index})',
                    visual_style="bold_border",
                    data_style="fiat",
                )
                self._fill_cell(
                    asset_exchange_sheet,
                    asset_exchange_row_index,
                    10,
                    f"=(I{asset_exchange_row_index+1}-F{asset_exchange_row_index+1})/F{asset_exchange_row_index+1}",
                    visual_style="bold_border",
                    data_style="percent",
                )
                self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 11, "", visual_style="bold_border")
                self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 12, "", visual_style="bold_border")
                row_indexes[_ASSET_EXCHANGE] = asset_exchange_row_index + 1

        asset_exchange_sheet.append_rows(1)
        asset_exchange_row_index = row_indexes[_ASSET_EXCHANGE]
        last_data_index = last_data_row_indexes[_ASSET_EXCHANGE]
        self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 0, _("Grand Total"), visual_style="bold_border")
        self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 1, "", visual_style="bold_border")
        self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 2, "", visual_style="bold_border")
        self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 3, "", visual_style="bold_border")
        self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 4, "", visual_style="bold_border")
        self._fill_cell(
            asset_exchange_sheet,
            asset_exchange_row_index,
            5,
            f"=SUM(F${self.HEADER_ROWS+1}:F${last_data_index})",
            visual_style="bold_border",
            data_style="fiat",
        )
        self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 6, "", visual_style="bold_border")
        self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 7, "", visual_style="bold_border")
        self._fill_cell(
            asset_exchange_sheet,
            asset_exchange_row_index,
            8,
            f"=SUM(I${self.HEADER_ROWS+1}:I${last_data_index})",
            visual_style="bold_border",
            data_style="fiat",
        )
        self._fill_cell(
            asset_exchange_sheet,
            asset_exchange_row_index,
            9,
            f"=SUM(J${self.HEADER_ROWS+1}:J${last_data_index})",
            visual_style="bold_border",
            data_style="fiat",
        )
        self._fill_cell(
            asset_exchange_sheet,
            asset_exchange_row_index,
            10,
            f"=(I{asset_exchange_row_index+1}-F{asset_exchange_row_index+1})/F{asset_exchange_row_index+1}",
            visual_style="bold_border",
            data_style="percent",
        )
        self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 11, "", visual_style="bold_border")
        self._fill_cell(asset_exchange_sheet, asset_exchange_row_index, 12, "", visual_style="bold_border")
        row_indexes[_ASSET_EXCHANGE] = asset_exchange_row_index + 1

        asset_sheet.name = _("Asset")
        asset_exchange_sheet.name = _("Asset - Exchange")
        input_sheet.name = _("Input")

        output_file.save()
        LOGGER.info("Plugin '%s' output: %s", __name__, Path(output_file.docname).resolve())
