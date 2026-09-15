# Practical Data Wrangling


Data is essential in data-driven projects, as it forms the foundation for all subsequent analysis, modeling, and decision-making. Depending on the specific task, raw data may be collected from a wide variety of sources such as databases, APIs, sensors, logs, documents, or images. Before it can be effectively used for analysis or machine learning, raw data must be cleaned, transformed, validated, and organized into a consistent and usable format. As data comes in many different forms, including numerical, categorical, time series, text, event/log, and image data, the tools and techniques used for data wrangling can vary significantly depending on the data type and the requirements of the task.

In this workshop, we will cover practical data wrangling techniques for numerical, categorical, time series, text, and image data. Participants will learn how to detect and handle missing values, outliers, inconsistencies, duplicates, and formatting problems. We will demonstrate methods for transforming and encoding categorical variables, parsing and aggregating temporal data, processing unstructured text, and preparing image datasets for machine learning and analytics. Each session combines concepts, demonstrations, and hands-on exercises using realistic datasets to help participants develop practical skills that can be applied immediately in downstream modeling tasks.

This workshop is designed for data practitioners who regularly work with raw or semi-structured data and need to prepare it for analysis or modeling, including data analysts, data scientists, machine learning engineers, and software engineers looking to strengthen their practical data preprocessing skills, as well as researchers and engineers working with real-world datasets who need a structured approach to data cleaning and transformation.



:::{prereq}

- Familiarity with Python basics (lists, dictionaries, loops, functions) and libraries like NumPy, Pandas, and Matplotlib/Seaborn.
- Be familiar with tabular data, rows and columns, missing values, data types, and basic descriptive statistics.
- Have introductory experience using NumPy and pandas for loading, inspecting, filtering, transforming, and summarizing data.
- Elementary understanding of statistics (mean, variance, correlation, basic probability).
- Basic command-line or Jupyter Notebook experience (navigating files, running scripts, installing packages).
:::



:::{toctree}
:caption: Software Setup
:maxdepth: 1

env/0-setting-up
:::



:::{toctree}
:caption: Lesson Episodes
:maxdepth: 1

episodes/1-getting-to-know-your-data
episodes/2-handling-numerical-data
episodes/3-processing-categorical-data
episodes/4-exploring-dates-times-and-time-series-data
episodes/5-wrangling-text-data
episodes/6-transforming-image-data
:::



::::{admonition} License
:class: attention

:::{admonition} CC BY-SA for media and pedagogical material
:class: attention dropdown

Copyright © 2026 ENCCS. This material is released by ENCCS under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).
- **Canonical URL**: <https://creativecommons.org/licenses/by-sa/4.0/>
- [See the legal code](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)

## You are free to

1. **Share** — copy and redistribute the material in any medium or format for any purpose, even commercially.
2. **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.
3. The licensor cannot revoke these freedoms as long as you follow the license terms.

## Under the following terms

1. **Attribution** — You must give [appropriate credit](https://creativecommons.org/licenses/by-sa/4.0/#ref-appropriate-credit) , provide a link to the license, and [indicate if changes were made](https://creativecommons.org/licenses/by-sa/4.0/#ref-indicate-changes) . You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
2. **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the [same license](https://creativecommons.org/licenses/by-sa/4.0/#ref-same-license) as the original.
3. **No additional restrictions** — You may not apply legal terms or [technological measures](https://creativecommons.org/licenses/by-sa/4.0/#ref-technological-measures) that legally restrict others from doing anything the license permits.

## Notices

You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable [exception or limitation](https://creativecommons.org/licenses/by/4.0/deed.en#ref-exception-or-limitation) .

No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as [publicity, privacy, or moral rights](https://creativecommons.org/licenses/by/4.0/deed.en#ref-publicity-privacy-or-moral-rights) may limit how you use the material.

This deed highlights only some of the key features and terms of the actual license. It is not a license and has no legal value. You should carefully review all of the terms and conditions of the actual license before using the licensed material.

:::

:::{admonition} MIT for source code and code snippets
:class: attention dropdown

MIT License

Copyright (c) 2026, ENCCS project, {{author}}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
:::

::::