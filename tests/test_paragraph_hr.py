from conftest import compare_have_want_handrails


def test_paragraph_with_mathblock_ending_with_text():
    compare_have_want_handrails(
        have="""
        :manuscript:

        This is a paragraph with math inside of it
        $$
        2+2=4,
        $$
        and it ends with text.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="1">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">

        <p>This is a paragraph with math inside of it </p>
        <div class="mathblock hr hr-hidden hr-offset" tabindex=0 data-nodeid="3">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Equation (1)</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">
        $$
        2+2=4,
        $$
        </div>

        <div class="hr-info-zone">
        <div class="hr-info"><div class="eqn-number"><p>(1)</p></div></div>
        </div>

        </div>
        <p> and it ends with text.</p>
        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_paragraph_ending_with_mathblock():
    compare_have_want_handrails(
        have="""
        :manuscript:

        This is a paragraph with math inside of it
        $$
        2+2=4.
        $$

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="1">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">

        <p>This is a paragraph with math inside of it </p>
        <div class="mathblock hr hr-hidden hr-offset" tabindex=0 data-nodeid="3">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Equation (1)</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">
        $$
        2+2=4.
        $$
        </div>

        <div class="hr-info-zone">
        <div class="hr-info"><div class="eqn-number"><p>(1)</p></div></div>
        </div>

        </div>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_paragraph_with_icon_ending_with_mathblock():
    compare_have_want_handrails(
        have=r"""
        :manuscript:

        :paragraph: {:icon: heart} Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
        do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        $$
        \left( \mathbf{B} \mathbf{v} \right)_{i \to j} = \sum_{k \to i \in \vec{E}}
        \mathbf{v}_{k \to i} - \mathbf{v}_{j \to i}.
        $$


        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="1">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">

        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
        <div class="mathblock hr hr-hidden hr-offset" tabindex=0 data-nodeid="3">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Equation (1)</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">
        $$
        \left( \mathbf{B} \mathbf{v} \right)_{i \to j} = \sum_{k \to i \in \vec{E}}
        \mathbf{v}_{k \to i} - \mathbf{v}_{j \to i}.
        $$
        </div>

        <div class="hr-info-zone">
        <div class="hr-info"><div class="eqn-number"><p>(1)</p></div></div>
        </div>

        </div>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info">
                        <div class="icon-wrapper heart">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="1 1 22 22" fill="#3C4952" class="icon icon-tabler icons-tabler-filled icon-tabler-heart">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                <path d="M6.979 3.074a6 6 0 0 1 4.988 1.425l.037 .033l.034 -.03a6 6 0 0 1 4.733 -1.44l.246 .036a6 6 0 0 1 3.364 10.008l-.18 .185l-.048 .041l-7.45 7.379a1 1 0 0 1 -1.313 .082l-.094 -.082l-7.493 -7.422a6 6 0 0 1 3.176 -10.215z" />
                </svg>
                        </div>
                        </div>
        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_paragraph_with_icon_with_mathblock_ending_with_text():
    compare_have_want_handrails(
        have=r"""
        :manuscript:

        :paragraph: {:icon: heart} Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
        do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        $$
        \left( \mathbf{B} \mathbf{v} \right)_{i \to j} = \sum_{k \to i \in \vec{E}}
        \mathbf{v}_{k \to i} - \mathbf{v}_{j \to i}.
        $$
        Lorem ipsum.

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="1">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">

        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
        <div class="mathblock hr hr-hidden hr-offset" tabindex=0 data-nodeid="3">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Equation (1)</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">
        $$
        \left( \mathbf{B} \mathbf{v} \right)_{i \to j} = \sum_{k \to i \in \vec{E}}
        \mathbf{v}_{k \to i} - \mathbf{v}_{j \to i}.
        $$
        </div>

        <div class="hr-info-zone">
        <div class="hr-info"><div class="eqn-number"><p>(1)</p></div></div>
        </div>

        </div>
        <p> Lorem ipsum.</p>
        </div>

        <div class="hr-info-zone">
        <div class="hr-info">
                        <div class="icon-wrapper heart">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="1 1 22 22" fill="#3C4952" class="icon icon-tabler icons-tabler-filled icon-tabler-heart">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                <path d="M6.979 3.074a6 6 0 0 1 4.988 1.425l.037 .033l.034 -.03a6 6 0 0 1 4.733 -1.44l.246 .036a6 6 0 0 1 3.364 10.008l-.18 .185l-.048 .041l-7.45 7.379a1 1 0 0 1 -1.313 .082l-.094 -.082l-7.493 -7.422a6 6 0 0 1 3.176 -10.215z" />
                </svg>
                        </div>
                        </div>
        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_paragraphs_with_icon():
    compare_have_want_handrails(
        have=r"""
        :manuscript:

        :paragraph: {:icon: heart} Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
        do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        $$
        \left( \mathbf{B} \mathbf{v} \right)_{i \to j} = \sum_{k \to i \in \vec{E}}
        \mathbf{v}_{k \to i} - \mathbf{v}_{j \to i}.
        $$
        Lorem ipsum.

        :paragraph: {:icon: success} Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat.

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="1">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">

        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
        <div class="mathblock hr hr-hidden hr-offset" tabindex=0 data-nodeid="3">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Equation (1)</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">
        $$
        \left( \mathbf{B} \mathbf{v} \right)_{i \to j} = \sum_{k \to i \in \vec{E}}
        \mathbf{v}_{k \to i} - \mathbf{v}_{j \to i}.
        $$
        </div>

        <div class="hr-info-zone">
        <div class="hr-info"><div class="eqn-number"><p>(1)</p></div></div>
        </div>

        </div>
        <p> Lorem ipsum.</p>
        </div>

        <div class="hr-info-zone">
        <div class="hr-info">
                        <div class="icon-wrapper heart">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="1 1 22 22" fill="#3C4952" class="icon icon-tabler icons-tabler-filled icon-tabler-heart">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                <path d="M6.979 3.074a6 6 0 0 1 4.988 1.425l.037 .033l.034 -.03a6 6 0 0 1 4.733 -1.44l.246 .036a6 6 0 0 1 3.364 10.008l-.18 .185l-.048 .041l-7.45 7.379a1 1 0 0 1 -1.313 .082l-.094 -.082l-7.493 -7.422a6 6 0 0 1 3.176 -10.215z" />
                </svg>
                        </div>
                        </div>
        </div>

        </div>

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="6">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">

        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info">
                        <div class="icon-wrapper success">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="2 2 20 20" fill="#3C4952" stroke-width="0" class="icon icon-tabler icons-tabler-filled icon-tabler-circle-check">
                <path d="M17 3.34a10 10 0 1 1 -14.995 8.984l-.005 -.324l.005 -.324a10 10 0 0 1 14.995 -8.336zm-1.293 5.953a1 1 0 0 0 -1.32 -.083l-.094 .083l-3.293 3.292l-1.293 -1.292l-.094 -.083a1 1 0 0 0 -1.403 1.403l.083 .094l2 2l.094 .083a1 1 0 0 0 1.226 0l.094 -.083l4 -4l.083 -.094a1 1 0 0 0 -.083 -1.32z" />
                </svg>
                        </div>
                        </div>
        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_paragraphs_with_icon_no_mathblock():
    compare_have_want_handrails(
        have=r"""
        :manuscript:

        :paragraph: {:icon: heart} Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
        do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

        :paragraph: {:icon: success} Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat.

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="1">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">

        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info">
                        <div class="icon-wrapper heart">
                        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="1 1 22 22" fill="#3C4952" class="icon icon-tabler icons-tabler-filled icon-tabler-heart">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                <path d="M6.979 3.074a6 6 0 0 1 4.988 1.425l.037 .033l.034 -.03a6 6 0 0 1 4.733 -1.44l.246 .036a6 6 0 0 1 3.364 10.008l-.18 .185l-.048 .041l-7.45 7.379a1 1 0 0 1 -1.313 .082l-.094 -.082l-7.493 -7.422a6 6 0 0 1 3.176 -10.215z" />
                </svg>
                        </div>
                        </div>
        </div>

        </div>

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="3">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item link disabled">
            <span class="icon-wrapper link">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 12.0003L12 6.00031M8 3.00031L8.463 2.46431C9.40081 1.52663 10.6727 0.999906 11.9989 1C13.325 1.00009 14.5968 1.527 15.5345 2.46481C16.4722 3.40261 16.9989 4.6745 16.9988 6.00066C16.9987 7.32682 16.4718 8.59863 15.534 9.53631L15 10.0003M10.0001 15.0003L9.60314 15.5343C8.65439 16.4725 7.37393 16.9987 6.03964 16.9987C4.70535 16.9987 3.42489 16.4725 2.47614 15.5343C2.0085 15.0719 1.63724 14.5213 1.38385 13.9144C1.13047 13.3076 1 12.6565 1 11.9988C1 11.3412 1.13047 10.69 1.38385 10.0832C1.63724 9.47628 2.0085 8.92571 2.47614 8.46331L3.00014 8.00031" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Copy link</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper tree">
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M3.57525 14.0448L6.00051 10.36M7.78824 7.64238L10.211 3.95918M7.79153 10.364L10.2134 14.044M12.0004 3.96001L14.4265 7.64801M4.36842 15.4C4.36842 14.9757 4.19098 14.5687 3.87513 14.2686C3.55928 13.9686 3.13089 13.8 2.68421 13.8C2.23753 13.8 1.80914 13.9686 1.49329 14.2686C1.17744 14.5687 1 14.9757 1 15.4C1 15.8243 1.17744 16.2313 1.49329 16.5314C1.80914 16.8314 2.23753 17 2.68421 17C3.13089 17 3.55928 16.8314 3.87513 16.5314C4.19098 16.2313 4.36842 15.8243 4.36842 15.4ZM12.7895 2.6C12.7895 2.17565 12.612 1.76869 12.2962 1.46863C11.9803 1.16857 11.5519 1 11.1053 1C10.6586 1 10.2302 1.16857 9.91435 1.46863C9.5985 1.76869 9.42105 2.17565 9.42105 2.6C9.42105 3.02435 9.5985 3.43131 9.91435 3.73137C10.2302 4.03143 10.6586 4.2 11.1053 4.2C11.5519 4.2 11.9803 4.03143 12.2962 3.73137C12.612 3.43131 12.7895 3.02435 12.7895 2.6ZM12.7895 15.4C12.7895 14.9757 12.612 14.5687 12.2962 14.2686C11.9803 13.9686 11.5519 13.8 11.1053 13.8C10.6586 13.8 10.2302 13.9686 9.91435 14.2686C9.5985 14.5687 9.42105 14.9757 9.42105 15.4C9.42105 15.8243 9.5985 16.2313 9.91435 16.5314C10.2302 16.8314 10.6586 17 11.1053 17C11.5519 17 11.9803 16.8314 12.2962 16.5314C12.612 16.2313 12.7895 15.8243 12.7895 15.4ZM8.57895 9C8.57895 8.57565 8.4015 8.16869 8.08565 7.86863C7.7698 7.56857 7.34142 7.4 6.89474 7.4C6.44806 7.4 6.01967 7.56857 5.70382 7.86863C5.38797 8.16869 5.21053 8.57565 5.21053 9C5.21053 9.42435 5.38797 9.83131 5.70382 10.1314C6.01967 10.4314 6.44806 10.6 6.89474 10.6C7.34142 10.6 7.7698 10.4314 8.08565 10.1314C8.4015 9.83131 8.57895 9.42435 8.57895 9ZM17 9C17 8.57565 16.8226 8.16869 16.5067 7.86863C16.1909 7.56857 15.7625 7.4 15.3158 7.4C14.8691 7.4 14.4407 7.56857 14.1249 7.86863C13.809 8.16869 13.6316 8.57565 13.6316 9C13.6316 9.42435 13.809 9.83131 14.1249 10.1314C14.4407 10.4314 14.8691 10.6 15.3158 10.6C15.7625 10.6 16.1909 10.4314 16.5067 10.1314C16.8226 9.83131 17 9.42435 17 9Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Tree</span>
          </div>

          <div class="hr-menu-item">
            <span class="icon-wrapper code">
              <svg width="18" height="16" viewBox="0 0 18 16" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.55556 4.5L1 8L4.55556 11.5M13.4444 4.5L17 8L13.4444 11.5M10.7778 1L7.22222 15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <span class="hr-menu-item-text">Source</span>
          </div>

        </div>

        </div>

        <div class="hr-border-zone">

                        <div class="hr-border-dots">
                          <div class="icon-wrapper">
                            <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="10 3 4 18"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-dots-vertical">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 19m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                              <path d="M12 5m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0" />
                            </svg>
                          </div>
                        </div>
                        <div class="hr-border-rect">
                        </div>

        </div>

        <div class="hr-spacer-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-content-zone">

        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info">
                        <div class="icon-wrapper success">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="2 2 20 20" fill="#3C4952" stroke-width="0" class="icon icon-tabler icons-tabler-filled icon-tabler-circle-check">
                <path d="M17 3.34a10 10 0 1 1 -14.995 8.984l-.005 -.324l.005 -.324a10 10 0 0 1 14.995 -8.336zm-1.293 5.953a1 1 0 0 0 -1.32 -.083l-.094 .083l-3.293 3.292l-1.293 -1.292l-.094 -.083a1 1 0 0 0 -1.403 1.403l.083 .094l2 2l.094 .083a1 1 0 0 0 1.226 0l.094 -.083l4 -4l.083 -.094a1 1 0 0 0 -.083 -1.32z" />
                </svg>
                        </div>
                        </div>
        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
