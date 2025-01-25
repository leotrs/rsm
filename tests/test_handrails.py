from conftest import compare_have_want_handrails


def test_manuscript():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        Hello.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Title</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h1>Some Title</h1>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

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

          <div class="hr-menu-item">
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

        <p>Hello.</p>

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


def test_section():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        # Section
        Hello.

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Title</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h1>Some Title</h1>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <section class="section level-2" data-nodeid="1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Section 1</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h2>1. Section</h2>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="2">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>Hello.</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_abstract():
    compare_have_want_handrails(
        have="""
        :manuscript:
        :title: Some Title

        :abstract:
          The abstract.
        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Title</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h1>Some Title</h1>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="abstract" data-nodeid="1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Abstract</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h3>Abstract</h3>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="2">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>The abstract.</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_theorem():
    compare_have_want_handrails(
        have="""
        :manuscript:

        :theorem:

        Hello.

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="theorem hr hr-labeled" tabindex=0 data-nodeid="1">

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Theorem 1</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <div class="paragraph hr-label">

        <p><span class="span"><strong>Theorem 1.</strong></span></p>

        </div>

        <div class="paragraph hr hr-offset hr-hidden" tabindex=0 data-nodeid="2">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>Hello.</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
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


def test_author():
    compare_have_want_handrails(
        have=r"""
        :manuscript:
          :title: Indefinite Linear Algebra of the NBM
          :date: 2024-04-13


        :author:
          :name: Leo Torres
          :email: leo@leotrs.com
        ::

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Title</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h1>Indefinite Linear Algebra of the NBM</h1>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="author hr hr-hidden" tabindex=0 data-nodeid="1">

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Author</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>Leo Torres</p>

        <p><a href="mailto:leo@leotrs.com">leo@leotrs.com</a></p>

        </div>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_toc_no_labels():
    compare_have_want_handrails(
        have="""
        :manuscript:
          :title: Foo

        :abstract:
          Abs.
        ::

        :toc:

        # Section

        ::

        # Section

        ## Sub-section

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">
        <div class="float-minimap-wrapper">
        <div class="minimap">

                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 104" fill="#3C4952" stroke-width="0">
                  <defs>

                    <linearGradient id="purple-green-scroll" x1="0%" x2="0%" y1="0%" y2="100%" gradientUnits="userSpaceOnUse">
                      <stop offset="0%" stop-color="#AD71F2" />
                      <stop id="stop-follow-scroll-1" offset="100%" stop-color="#1FB5A2" />
                      <stop id="stop-follow-scroll-2" offset="100%" stop-color="#DAE1E5" />
                      <stop offset="100%" stop-color="#DAE1E5" />
                    </linearGradient>

                    <mask id="gradient-mask">
                      <rect width="100%" height="100%" fill="url(#purple-green-scroll)" />
                    </mask>

                  </defs>

                  <g fill="url(#purple-green-scroll)">
                    <rect x="12" width="8" height="104" />
            <circle id="mm-" cx="16" cy="20" r="8" />
            <circle cx="16" cy="20" r="3" fill="#FCFEFF" />
            <circle id="mm-" cx="16" cy="52" r="8" />
            <circle cx="16" cy="52" r="3" fill="#FCFEFF" />
            <circle id="mm-" cx="16" cy="84" r="6" />
            <circle cx="16" cy="84" r="3" fill="#FCFEFF" /><g>
        </svg>
        </div>
        </div>
        <section class="level-1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Title</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h1>Foo</h1>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="abstract" data-nodeid="1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Abstract</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h3>Abstract</h3>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="2">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>Abs.</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </div>

        <div class="toc">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Contents</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h3>Table of Contents</h3>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="toc-wrapper">

        <div class="minimap">

                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 104" fill="#3C4952" stroke-width="0">
                  <defs>

                    <linearGradient id="purple-green-mouse" x1="0%" x2="0%" y1="0%" y2="100%" gradientUnits="userSpaceOnUse">
                      <stop offset="0%" stop-color="#AD71F2" />
                      <stop id="stop-follow-mouse-1" offset="100%" stop-color="#1FB5A2" />
                      <stop id="stop-follow-mouse-2" offset="100%" stop-color="#DAE1E5" />
                      <stop offset="100%" stop-color="#DAE1E5" />
                    </linearGradient>

                    <mask id="gradient-mask">
                      <rect width="100%" height="100%" fill="url(#purple-green-mouse)" />
                    </mask>

                  </defs>

                  <g fill="url(#purple-green-mouse)">
                    <rect x="12" width="8" height="104" />
            <circle cx="16" cy="20" r="8" />
            <circle cx="16" cy="20" r="3" fill="#FCFEFF" />
            <circle cx="16" cy="52" r="8" />
            <circle cx="16" cy="52" r="3" fill="#FCFEFF" />
            <circle cx="16" cy="84" r="6" />
            <circle cx="16" cy="84" r="3" fill="#FCFEFF" /><g>
        </svg>
        </div>

        <ul class="contents" data-nodeid="4">

        <li class="item" data-nodeid="5">
        <a class="reference" href="#">1. Section</a>
        </li>

        <li class="item" data-nodeid="7">
        <a class="reference" href="#">2. Section</a>
        <ul class="itemize" data-nodeid="9">

        <li class="item" data-nodeid="10">
        <a class="reference" href="#">2.1. Sub-section</a>
        </li>

        </ul>

        </li>

        </ul>

        </div>

        </div>

        <section class="section level-2" data-nodeid="12">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Section 1</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h2>1. Section</h2>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </section>

        <section class="section level-2" data-nodeid="13">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Section 2</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h2>2. Section</h2>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <section class="subsection level-3" data-nodeid="14">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Section 2.1</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h3>2.1. Sub-section</h3>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </section>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_toc_with_labels():
    compare_have_want_handrails(
        have="""
        :manuscript:
          :title: Foo

        :abstract:
          Abs.
        ::

        :toc:

        # Section
          :label: sec-1

        ::

        # Section
          :label: sec-2

        ## Sub-section
          :label: sub-sec

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">
        <div class="float-minimap-wrapper">
        <div class="minimap">

                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 104" fill="#3C4952" stroke-width="0">
                  <defs>

                    <linearGradient id="purple-green-scroll" x1="0%" x2="0%" y1="0%" y2="100%" gradientUnits="userSpaceOnUse">
                      <stop offset="0%" stop-color="#AD71F2" />
                      <stop id="stop-follow-scroll-1" offset="100%" stop-color="#1FB5A2" />
                      <stop id="stop-follow-scroll-2" offset="100%" stop-color="#DAE1E5" />
                      <stop offset="100%" stop-color="#DAE1E5" />
                    </linearGradient>

                    <mask id="gradient-mask">
                      <rect width="100%" height="100%" fill="url(#purple-green-scroll)" />
                    </mask>

                  </defs>

                  <g fill="url(#purple-green-scroll)">
                    <rect x="12" width="8" height="104" />
            <circle id="mm-sec-1" cx="16" cy="20" r="8" />
            <circle cx="16" cy="20" r="3" fill="#FCFEFF" />
            <circle id="mm-sec-2" cx="16" cy="52" r="8" />
            <circle cx="16" cy="52" r="3" fill="#FCFEFF" />
            <circle id="mm-sub-sec" cx="16" cy="84" r="6" />
            <circle cx="16" cy="84" r="3" fill="#FCFEFF" /><g>
        </svg>
        </div>
        </div>
        <section class="level-1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Title</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h1>Foo</h1>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="abstract" data-nodeid="1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Abstract</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h3>Abstract</h3>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="2">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>Abs.</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </div>

        <div class="toc">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Contents</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h3>Table of Contents</h3>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="toc-wrapper">

        <div class="minimap">

                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 104" fill="#3C4952" stroke-width="0">
                  <defs>

                    <linearGradient id="purple-green-mouse" x1="0%" x2="0%" y1="0%" y2="100%" gradientUnits="userSpaceOnUse">
                      <stop offset="0%" stop-color="#AD71F2" />
                      <stop id="stop-follow-mouse-1" offset="100%" stop-color="#1FB5A2" />
                      <stop id="stop-follow-mouse-2" offset="100%" stop-color="#DAE1E5" />
                      <stop offset="100%" stop-color="#DAE1E5" />
                    </linearGradient>

                    <mask id="gradient-mask">
                      <rect width="100%" height="100%" fill="url(#purple-green-mouse)" />
                    </mask>

                  </defs>

                  <g fill="url(#purple-green-mouse)">
                    <rect x="12" width="8" height="104" />
            <circle cx="16" cy="20" r="8" />
            <circle cx="16" cy="20" r="3" fill="#FCFEFF" />
            <circle cx="16" cy="52" r="8" />
            <circle cx="16" cy="52" r="3" fill="#FCFEFF" />
            <circle cx="16" cy="84" r="6" />
            <circle cx="16" cy="84" r="3" fill="#FCFEFF" /><g>
        </svg>
        </div>

        <ul class="contents" data-nodeid="4">

        <li class="item" data-nodeid="5">
        <a class="reference" href="#sec-1">1. Section</a>
        </li>

        <li class="item" data-nodeid="7">
        <a class="reference" href="#sec-2">2. Section</a>
        <ul class="itemize" data-nodeid="9">

        <li class="item" data-nodeid="10">
        <a class="reference" href="#sub-sec">2.1. Sub-section</a>
        </li>

        </ul>

        </li>

        </ul>

        </div>

        </div>

        <section id="sec-1" class="section level-2" data-nodeid="12">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Section 1</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h2>1. Section</h2>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </section>

        <section id="sec-2" class="section level-2" data-nodeid="13">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Section 2</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h2>2. Section</h2>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <section id="sub-sec" class="subsection level-3" data-nodeid="14">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Section 2.1</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h3>2.1. Sub-section</h3>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        </section>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_bibliography():
    compare_have_want_handrails(
        have="""
        :manuscript:

        This is a citation :cite:atiyah2018introduction::.

        :bibliography: ::

        ::

        :bibtex:

        @book{atiyah2018introduction,
          title={Introduction to commutative algebra},
          author={Atiyah, M.F., & MacDonald, I.G.},
          year={2018},
          publisher={CRC Press},
          doi={https://doi.org/10.1201/9780429493638},
        }

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

          <div class="hr-menu-item">
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

        <p>This is a citation [<a id="cite-0" class="reference" href="#atiyah2018introduction">1</a>].</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <section class="level-2">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Bibliography</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h2>References</h2>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <ol class="bibliography" data-nodeid="5">

        <li id="atiyah2018introduction" class="bibitem" data-nodeid="6">
        Atiyah, M.F., & MacDonald, I.G. "Introduction to commutative algebra". CRC Press. 2018. <a id="atiyah2018introduction-doi" class="bibitem-doi" href="https://doi.org/https://doi.org/10.1201/9780429493638" target="_blank">[link]</a><br />[<a class="reference backlink" href="#cite-0">^1</a>]
        </li>

        </ol>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_inline_math_followed_by_dot():
    compare_have_want_handrails(
        have="""
        :manuscript:
          :title: title

        :author:
          :name: Leo
        ::

        one $2+2=4$.

        two $2+2=4$ baz.

        three $2+2=4$. Another sentence.

        ::
        """,
        want=r"""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="heading hr" tabindex=0>

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Title</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <h1>title</h1>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="author hr hr-hidden" tabindex=0 data-nodeid="1">

        <div class="hr-collapse-zone">

                    <div class="hr-collapse">
                      <div class="icon-wrapper collapse">
                        <svg width="8" height="14" viewBox="0 0 8 14" fill="none" stroke="#3C4952" xmlns="http://www.w3.org/2000/svg">
                          <path d="M1 1L7 7L1 13" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </div>
                    </div>

        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Author</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>Leo</p>

        </div>

        </div>

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="2">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>one <span class="inline-math-wrapper">
        <span class="math" data-nodeid="4">\(2+2=4\)</span><span>.</span></span></p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="7">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>two <span class="math" data-nodeid="9">\(2+2=4\)</span> baz.</p>

        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
        </div>

        </div>

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="12">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>three <span class="inline-math-wrapper">
        <span class="math" data-nodeid="14">\(2+2=4\)</span><span>.</span></span> Another sentence.</p>

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


def test_mathblock_nonum():
    compare_have_want_handrails(
        have="""
        :manuscript:

        This one has a number
        $$
        2+2=4
        $$

        And this one does not
        $$
        :nonum:
        2+2=4
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

          <div class="hr-menu-item">
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

        <p>This one has a number </p>
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

          <div class="hr-menu-item">
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
        2+2=4
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

        <div class="paragraph hr hr-hidden" tabindex=0 data-nodeid="5">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Paragraph</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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

        <p>And this one does not </p>
        <div class="mathblock hr hr-hidden hr-offset" tabindex=0 data-nodeid="7">

        <div class="hr-collapse-zone">
        <div class="hr-spacer"></div>
        </div>

        <div class="hr-menu-zone">

        <div class="hr-menu">

          <div class="hr-menu-label">
            <span class="hr-menu-item-text">Equation (None)</span>
          </div>

          <div class="hr-menu-separator"></div>

          <div class="hr-menu-item">
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
        2+2=4
        $$
        </div>

        <div class="hr-info-zone">
        <div class="hr-info"></div>
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
